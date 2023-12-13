// g++ 12_c++.cpp -std=c++20 -Ofast -o out && ./out

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <numeric>
#include <chrono>
#include <algorithm>
#include <stdint.h>


using namespace std;
using namespace std::chrono;


// int springs_size;
// vector<char> springs;
// vector<int> constraints;
// inline int64_t recurse(int spring_index, int constraint_index, int to_place) {
//     if (to_place == 0) {
//         for (; spring_index < springs_size; ++spring_index) {
//             if (springs[spring_index] == '#') {
//                 return 0;
//             }
//         }
//         return 1;
//     }
//     int spaces_left = springs_size - spring_index;
//     if (to_place > spaces_left) {
//         return 0;
//     }
    
//     int64_t total = 0;
//     if (springs[spring_index] != '#') {
//         total += recurse(spring_index + 1, constraint_index, to_place);
//     }

//     int num = constraints[constraint_index];
//     if (springs[spring_index] != '.') {
//         int checking = spring_index;
//         while (checking < spring_index + num) {
//             if (springs[checking] == '.') {
//                 return total;
//             }
//             checking++;
//         }
//         if (checking == springs_size || springs[checking] != '#') {
//             total += recurse(checking + 1, constraint_index + 1, to_place - num);   
//         }
//     }
//     return total;
// }


vector<char> springs;
vector<int> constraints;

vector<vector<int>> can_index_fit_n_springs;
vector<int64_t> no_hashes_left;
void init_precompute() {
    can_index_fit_n_springs.clear();
    no_hashes_left.clear();

    for (int spring_index = 0; spring_index < springs.size(); spring_index++) {
        can_index_fit_n_springs.push_back(vector<int>());
        can_index_fit_n_springs[spring_index].push_back(1);
        for (int num_springs = 1; num_springs < (springs.size() + 1) - spring_index; num_springs++) {
            int ans = 1;
            int k;
            for (k = spring_index; k < spring_index + num_springs; k++) {
                if (springs[k] == '.') {
                    ans = 0;
                }
            }
            if (k < springs.size() && springs[k] == '#') {
                ans = 0;
            }
            can_index_fit_n_springs[spring_index].push_back(ans);
        }

        int64_t tracker = 1;
        for (int z = spring_index; z < springs.size(); z++) {
            if (springs[z] == '#') {
                tracker = 0;
            }
        }
        no_hashes_left.push_back(tracker);
    }
    no_hashes_left.push_back(1);
    no_hashes_left.push_back(1);
}


int springs_size;
inline int64_t recurse(int spring_index, int constraint_index, int to_place) {
    if (to_place == 0) {
        return no_hashes_left[spring_index];
    }
    int spaces_left = springs_size - spring_index;
    if (to_place > spaces_left) {
        return 0;
    }
    
    int64_t total = 0;
    if (springs[spring_index] != '#') {
        total += recurse(spring_index + 1, constraint_index, to_place);
    }

    int num = constraints[constraint_index];
    if (springs[spring_index] != '.') {
        if (can_index_fit_n_springs[spring_index][num]) {
            total += recurse(spring_index + num + 1, constraint_index + 1, to_place - num);   
        }
    }
    return total;
}


int main() {
    int64_t total = 0;
    int curr_line = 0;
    ifstream file("12.dat");
    string line;
    auto start = high_resolution_clock::now();

    int duplications = 3;
    // 3 - Total possiblities: 127369793, in 1897ms         (1.9 seconds)
    // Duplications: 4, Total possiblities: 55726203441, in (923 seconds)

    while (getline(file, line)) {
        if (line.length() < 1) {
            continue;
        }
        curr_line++;
        
        vector<char> springs_file;
        int index = 0;
        while (line[index] != ' ') {
            springs_file.push_back(line[index]);
            index++;
        }

        vector<int> constraints_file;
        string after_springs = line.substr(index + 1);
        stringstream after_springs_stream(after_springs);
        string temp;
        while (getline(after_springs_stream, temp, ',')) {
            constraints_file.push_back(atoi(temp.c_str()));
        }

        vector<char> springs_dup;
        vector<int> constraints_dup;
        for (int i = 0; i < duplications; i++) {
            springs_dup.insert(springs_dup.end(), springs_file.begin(), springs_file.end());
            if (i != duplications - 1) {
                springs_dup.push_back('?');
            }
            constraints_dup.insert(constraints_dup.end(), constraints_file.begin(), constraints_file.end());
        }

        // i think this optimization hardly helps
        auto first = find(springs_dup.begin(), springs_dup.end(), '?');
        int dist_start = (first != springs_dup.end()) ? distance(springs_dup.begin(), first) : -1;
        auto last = find(springs_dup.rbegin(), springs_dup.rend(), '?');
        int dist_end = (last != springs_dup.rend()) ? distance(last, springs_dup.rend()) - 1 : -1;
        if (dist_end < dist_start) {
            reverse(springs_dup.begin(), springs_dup.end());
            reverse(constraints_dup.begin(), constraints_dup.end());
        }

        cout << "INTITAL: Springs: ";
        for (auto i: springs_dup) {
            cout << i;
        } 
        cout << ", Other: ";
        for (auto i: constraints_dup) {
            cout << i << ", ";
        }
        cout << endl;

        springs_size = springs_dup.size();
        springs = springs_dup;
        constraints = constraints_dup;
        init_precompute();
        int64_t return_val = recurse(0, 0, reduce(constraints_dup.begin(), constraints_dup.end()));
        total += return_val;

        cout << "Total for " << curr_line << ": " << return_val << endl;
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Duplications: " << duplications << ", Total possiblities: " << total << ", in " << duration.count() << "ms" << endl;
    return 0;
}


// auto last_hash = find(springs_dup.rbegin(), springs_dup.rend(), '#');
// int last_hash_index = (last_hash == springs_dup.rend()) ? -1: -(distance(springs_dup.rend(), last_hash) + 1);


// int counter = 0;
// for (auto vec: can_index_fit_n_springs) {
//     cout << counter << ": ";
//     for (auto ele: vec) {
//         cout << ele;
//     }
//     cout << endl;
//     counter++;
// }

// break;
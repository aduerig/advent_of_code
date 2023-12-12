// g++ 12_c++.cpp -std=c++20 -Ofast -o out && ./out

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <numeric>
#include <chrono>
#include <algorithm>


using namespace std;
using namespace std::chrono;

int recurse(vector<char> springs, int spring_index, vector<int> constraints, int constraint_index, int to_place) {
    if (to_place == 0) {
        while (spring_index < springs.size()) {
            if (springs[spring_index] == '#') {
                return 0;
            }
            spring_index++;
        }
        return 1;
    }

    int spaces_left = springs.size() - spring_index;
    if (to_place > spaces_left) {
        return 0;
    }
    
    int condition = springs[spring_index];
    int num = constraints[constraint_index];
    int total = 0;
    if (condition != '#') {
        total += recurse(springs, spring_index + 1, constraints, constraint_index, to_place);
    }

    if (condition != '.') {
        int start = 0;
        while (start < num) {
            if (springs[start + spring_index] == '.') {
                return total;
            }
            start += 1;
        }
        if (num == spaces_left || springs[num + spring_index] != '#') {
            total += recurse(springs, spring_index + num + 1, constraints, constraint_index + 1, to_place - num);   
        }
    }
    return total;
}

int main() {
    int total = 0;
    int curr_line = 0;
    ifstream file("12.dat");
    string line;
    auto start = high_resolution_clock::now();
    while (getline(file, line)) {
        if (line.length() < 1) {
            continue;
        }

        curr_line++;
        // if (curr_line != 289) {
        //     continue;
        // }

        // with reverse all: 39s
        // without reverse all: 39s

        int duplications = 3;

        vector<char> springs;
        int index = 0;
        while (line[index] != ' ') {
            springs.push_back(line[index]);
            index++;
        }

        vector<int> constraints;
        string after_springs = line.substr(index + 1);
        stringstream after_springs_stream(after_springs);
        string temp;
        while (getline(after_springs_stream, temp, ',')) {
            constraints.push_back(atoi(temp.c_str()));
        }

        vector<char> springs_dup;
        vector<int> constraints_dup;
        for (int i = 0; i < duplications; i++) {
            springs_dup.insert(springs_dup.end(), springs.begin(), springs.end());
            if (i != duplications - 1) {
                springs_dup.push_back('?');
            }
            constraints_dup.insert(constraints_dup.end(), constraints.begin(), constraints.end());
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

        int return_val = recurse(springs_dup, 0, constraints_dup, 0, reduce(constraints_dup.begin(), constraints_dup.end()));
        total += return_val;

        cout << "Total for " << curr_line << ": " << return_val << endl;
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Total possiblities: " << total << ", in " << duration.count() << "ms" << endl;
    return 0;
}
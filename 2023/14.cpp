// g++ 14.cpp -std=c++20 -Ofast -o out && ./out

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <numeric>
#include <chrono>
#include <algorithm>
#include <stdint.h>
#include <unordered_map>
#include <bits/stdc++.h>


using namespace std;
using namespace std::chrono;

vector<vector<char>> grid;
inline void roll_up() {
    for (int x = 0; x < grid[0].size(); x++) {
        int empty = 0;
        for (int y = 0; y < grid.size(); y++) {
            if (grid[y][x] == 'O') {
                grid[y][x] = '.';
                grid[empty][x] = 'O';
                empty += 1;
            }
            else if (grid[y][x] == '#') {
                empty = y + 1;
            }
        }
    }
}

inline void roll_down() {
    for (int x = 0; x < grid[0].size(); x++) {
        int empty = grid.size() - 1;
        for (int y = grid.size() - 1; y > -1; y--) {
            if (grid[y][x] == 'O') {
                grid[y][x] = '.';
                grid[empty][x] = 'O';
                empty -= 1;
            }
            else if (grid[y][x] == '#') {
                empty = y - 1;
            }
        }
    }
}

inline void roll_left() {
    for (int y = 0; y < grid.size(); y++) {
        int empty = 0;
        for (int x = 0; x < grid[0].size(); x++) {
            if (grid[y][x] == 'O') {
                grid[y][x] = '.';
                grid[y][empty] = 'O';
                empty += 1;
            }
            else if (grid[y][x] == '#') {
                empty = x + 1;
            }
        }
    }
}

inline void roll_right() {
    for (int y = 0; y < grid.size(); y++) {
        int empty = grid[0].size() - 1;
        for (int x = grid[0].size() - 1; x > -1; x--) {
            if (grid[y][x] == 'O') {
                grid[y][x] = '.';
                grid[y][empty] = 'O';
                empty -= 1;
            }
            else if (grid[y][x] == '#') {
                empty = x - 1;
            }
        }
    }
}


void roll_all() {
    roll_up();
    roll_left();
    roll_down();
    roll_right();
}

int main() {
    ifstream file("14.dat");
    string line;
    auto start = high_resolution_clock::now();

    while (getline(file, line)) {
        grid.push_back(vector<char>(line.begin(), line.end()));
    }

    for (size_t i = 0; i < 1000000000; i++) {
        if (i % 100000 == 0 && i != 0) {
            auto interim_time = high_resolution_clock::now();
            auto interim_duration = duration_cast<seconds>(interim_time - start);
            auto rate = (double) i / (double) interim_duration.count();
            cout << i << ", " << rate << " iterations/second will take: " << ((1000000000 - i) / rate) / (60 * 60) << " hours to complete" << endl;
        }
        roll_all();
    }

    int total = 0;
    for (size_t i = 0; i < grid.size(); i++) {
        total += (grid.size() - i) * count(grid[i].begin(), grid[i].end(), 'O');
    }


    auto end = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(end - start);
    cout << total << ", " << duration.count() << " seconds taken" << endl;
    return 0;
}
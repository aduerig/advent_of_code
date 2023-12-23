// g++ 23.cpp -std=c++20 -Ofast -o out && ./out

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <chrono>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <string>
#include <stdint.h>

using namespace std;
using namespace std::chrono;

vector<pair<int, int>> dirs = {
    make_pair(1, 0),
    make_pair(-1, 0), 
    make_pair(0, 1), 
    make_pair(0, -1),
};


int64_t nodes = 0;
auto start = high_resolution_clock::now();
inline int recurse(vector<vector<char>>& grid, vector<vector<bool>>& visited, pair<int, int>& pos, pair<int, int>& end, int steps) {
    nodes++;
    if (nodes % 100000 == 0 && nodes != 0) {
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end - start);
        auto rate = nodes / ((float) duration.count() / 1000);
        cout << nodes << " nodes explored. " << duration.count() << " milliseconds taken so far. " << rate << " nodes per second." << endl;
    }

    if (pos == end) {
        return steps;
    }

    auto&[x, y] = pos;
    visited[y][x] = true;

    int the_max = 0;
    for (auto& dpos: dirs) {
        auto&[dx, dy] = dpos;
        pair<int, int> new_pos = make_pair(x + dx, y + dy);
        auto&[new_x, new_y] = new_pos;

        if (new_x < 0 || new_y < 0 || new_x >= grid[0].size() || new_y >= grid.size()) {
            continue;
        }

        if (grid[new_y][new_x] == '#') {
            continue;
        }

        if (visited[new_y][new_x] == true) {
            continue;
        }
        
        the_max = max(the_max, recurse(grid, visited, new_pos, end, steps + 1));
    }

    visited[y][x] = false;
    return the_max;
}


int main() {
    ifstream file("23.dat");
    string line;

    vector<vector<char>> grid;
    vector<vector<bool>> visited;
    
    pair<int, int> end_pos, start_pos;
    
    int y = 0;
    while (getline(file, line)) {
        vector<char> new_row;
        vector<bool> visited_row;

        for (int x = 0; x < line.length(); x++) {
            if (line[x] == '.') {
                if (y == 0) {
                    start_pos = make_pair(x, y);
                }
                end_pos = make_pair(x, y);
            }
            new_row.push_back(line[x]);
            visited_row.push_back(false);
        }
        grid.push_back(new_row);
        visited.push_back(visited_row);
        y++;
    }

    cout << recurse(grid, visited, start_pos, end_pos, 0) << endl;


    auto end = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(end - start);
    cout << endl << duration.count() << " seconds taken" << endl;
    return 0;
}

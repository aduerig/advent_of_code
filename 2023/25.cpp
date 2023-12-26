// g++ 25.cpp -std=c++20 -Ofast -o out && ./out

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <string>
#include <stdint.h>
#include "veque.hpp"

using namespace std;
using namespace std::chrono;


inline std::string& rtrim(std::string& s, const char* t = " \t\n\r\f\v") {
    s.erase(s.find_last_not_of(t) + 1);
    return s;
}
inline std::string& ltrim(std::string& s, const char* t = " \t\n\r\f\v") {
    s.erase(0, s.find_first_not_of(t));
    return s;
}

inline std::string& trim(std::string& s, const char* t = " \t\n\r\f\v") {
    return ltrim(rtrim(s, t), t);
}

inline bool in(unordered_map<string, vector<string>>& the_map, string& the_ele) {
    return the_map.find(the_ele) != the_map.end();
}

inline bool in(unordered_map<string, int>& the_map, string& the_ele) {
    return the_map.find(the_ele) != the_map.end();
}

inline bool in(unordered_set<string>& the_set, string& the_ele) {
    return the_set.find(the_ele) != the_set.end();
}

inline bool in(unordered_set<int>& the_set, int the_ele) {
    return the_set.find(the_ele) != the_set.end();
}


struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int>& v) const {
        return v.first*31+v.second;
    }
};

inline bool my_in(const vector<pair<int, int>>& the_pairs, const pair<int, int>& the_ele) {
    return find(the_pairs.begin(), the_pairs.end(), the_ele) != the_pairs.end();
}



inline int visit_things(int curr, vector<vector<int>>& graph, vector<pair<int, int>>& bad_connections, vector<bool>& visited) {
    visited[curr] = true;
    int summer = 1;
    for (auto& node: graph[curr]) {
        if (visited[node] == true || my_in(bad_connections, make_pair(node, curr)) || my_in(bad_connections, make_pair(curr, node))) {
            continue;
        }
        summer += visit_things(node, graph, bad_connections, visited);
    }
    return summer;
}



int main() {
    ifstream file("25.dat");
    string line;

    unordered_map<string, int> string_to_int {};
    // unordered_map<int, string> int_to_string {};
    int unseen_int = 0;

    unordered_set<pair<int, int>, pair_hash> connections;

    vector<vector<int>> graph;
    unordered_set<int> nodes_set;
    while (getline(file, line)) {
        stringstream line_stream(line);
        
        string identifier;
        string outputs;

        getline(line_stream, identifier, ':');
        getline(line_stream, outputs, ':');


        if (!in(string_to_int, identifier)) {
            string_to_int[identifier] = unseen_int;
            unseen_int++;
            graph.push_back(vector<int>());
        }
        nodes_set.emplace(string_to_int[identifier]);

        outputs = trim(outputs);
        stringstream outputs_stream(outputs);
        string output_name;
        while (getline(outputs_stream, output_name, ' ')) {
            if (!in(string_to_int, output_name)) {
                string_to_int[output_name] = unseen_int;
                unseen_int++;
                graph.push_back(vector<int>());
            }
            graph[string_to_int[output_name]].push_back(string_to_int[identifier]);
            // cout << "output_name: " << output_name << ", identifier: " << identifier << endl;
            graph[string_to_int[identifier]].push_back(string_to_int[output_name]);
            if (string_to_int[output_name] < string_to_int[identifier]) {
                connections.emplace(make_pair(string_to_int[output_name], string_to_int[identifier]));
            } else {
                connections.emplace(make_pair(string_to_int[identifier], string_to_int[output_name]));
            }
            nodes_set.emplace(string_to_int[output_name]);
        }
    }
    auto start = high_resolution_clock::now();

    vector<pair<int, int>> connections_again (connections.begin(), connections.end());
    vector<int> nodes (nodes_set.begin(), nodes_set.end());
    for (int a = 0; a < connections_again.size(); a++) {
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<seconds>(end - start);
        cout << "a: " << a+1 << "/" << nodes.size() << ", " << duration.count() << " seconds taken" << endl;
        pair<int, int> a_ele = connections_again[a];
        for (int b = a+1; b < connections_again.size(); b++) {
            // cout << "b: " << b << endl;
            pair<int, int> b_ele = connections_again[b];
            for (int c = b+1; c < connections_again.size(); c++) {

                pair<int, int> c_ele = connections_again[c];
                vector<pair<int, int>> bad_connections = {
                    a_ele, b_ele, c_ele
                };
                vector<bool> visited(nodes.size(), false);
                int result = visit_things(0, graph, bad_connections, visited);
                if (nodes.size() != result) {
                    cout << result * (nodes.size() - result) << endl;
                    exit(0);
                }
            }
        }
    }

    // auto end = high_resolution_clock::now();
    // auto duration = duration_cast<seconds>(end - start);
    // cout << endl << duration.count() << " seconds taken" << endl;
    return 0;
}
// g++ 25_again.cpp -std=c++20 -Ofast -o out -g && ./out

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



vector<vector<int>> graph;
int summer = 0;
inline void visit_things(int curr, vector<bool>& visited) {
    visited[curr] = true;
    summer++;
    for (auto node: graph[curr]) {
        if (visited[node] == true) {
            continue;
        }
        visit_things(node, visited);
    }
}

inline void delete_thing(vector<int>& to_delete, int val) {
    auto it = std::find(to_delete.begin(), to_delete.end(), val);
    std::swap(*it, to_delete.back());
    to_delete.pop_back();
}

int main() {
    ifstream file("25.dat");
    string line;

    unordered_map<string, int> string_to_int {};
    unordered_map<int, string> int_to_string {};
    int unseen_int = 0;

    unordered_set<pair<int, int>, pair_hash> connections;

    unordered_set<int> nodes_set;
    while (getline(file, line)) {
        stringstream line_stream(line);
        
        string identifier;
        string outputs;

        getline(line_stream, identifier, ':');
        getline(line_stream, outputs, ':');


        if (!in(string_to_int, identifier)) {
            string_to_int[identifier] = unseen_int;
            int_to_string[unseen_int] = identifier;
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
                int_to_string[unseen_int] = output_name;
                unseen_int++;
                graph.push_back(vector<int>());
            }
            graph[string_to_int[output_name]].push_back(string_to_int[identifier]);
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
    // its on 718
    // dlv-tqh, ngp-bmd, grd-tqr

    vector<int> nodes (nodes_set.begin(), nodes_set.end());
    for (int a = 718; a < connections_again.size(); a++) {
        auto end = high_resolution_clock::now();
        auto duration = duration_cast<seconds>(end - start);
        cout << "a: " << a+1 << "/" << connections_again.size() << ", " << duration.count() << " seconds taken" << endl;
        pair<int, int> a_ele = connections_again[a];

        delete_thing(graph[a_ele.first], a_ele.second);
        delete_thing(graph[a_ele.second], a_ele.first);

        for (int b = a+1; b < connections_again.size(); b++) {
            // cout << "b: " << b+1 << "/" << connections_again.size() << endl;
            pair<int, int> b_ele = connections_again[b];
            delete_thing(graph[b_ele.first], b_ele.second);
            delete_thing(graph[b_ele.second], b_ele.first);


            for (int c = b+1; c < connections_again.size(); c++) {
                pair<int, int> c_ele = connections_again[c];
                delete_thing(graph[c_ele.first], c_ele.second);
                delete_thing(graph[c_ele.second], c_ele.first);

                vector<bool> visited(nodes.size(), false);
                summer = 0;
                visit_things(0, visited);

                if (nodes.size() != summer) {
                    cout << summer * (nodes.size() - summer) << endl;
                    cout << int_to_string[a_ele.first] << "-" << int_to_string[a_ele.second] << ", " << int_to_string[b_ele.first] << "-" << int_to_string[b_ele.second] << ", " << int_to_string[c_ele.first] << "-" << int_to_string[c_ele.second] << endl;
                    exit(0);
                }
                graph[c_ele.first].push_back(c_ele.second);
                graph[c_ele.second].push_back(c_ele.first);
            }
            graph[b_ele.first].push_back(b_ele.second);
            graph[b_ele.second].push_back(b_ele.first);

        }

        graph[a_ele.first].push_back(a_ele.second);
        graph[a_ele.second].push_back(a_ele.first);
    }
    return 0;
}
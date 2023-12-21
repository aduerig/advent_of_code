// g++ 20.cpp -std=c++20 -Ofast -o out && ./out

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

inline bool in(unordered_map<string, int>& the_map, string the_ele) {
    return the_map.find(the_ele) != the_map.end();
}

inline bool in(unordered_set<string>& the_set, string the_ele) {
    return the_set.find(the_ele) != the_set.end();
}

struct bfs_node {
    int from_name;
    int name;
    int signal;
};


void print_bfs_node(unordered_map<int, string>& the_map, bfs_node& node) {
    string to_print = "high";
    if (node.signal == 0) {
        to_print = "low";
    }
    cout << the_map[node.from_name] << " -" << to_print << "->" << " " << the_map[node.name] << endl;
}


int main() {
    ifstream file("20.dat");
    string line;

    unordered_map<string, vector<string>> all_outputs;
    unordered_set<string> conditionals;
    deque<tuple<string, string, int>> my_queue;
    while (getline(file, line)) {
        stringstream line_stream(line);
        
        string identifier;
        string outputs;

        getline(line_stream, identifier, '>');
        getline(line_stream, outputs, '>');

        identifier = identifier.substr(0, identifier.length() - 1);

        char condition_flip_or_broadcast = identifier[0];
        if (condition_flip_or_broadcast != 'b') {
            identifier = identifier.substr(1);
        }

        trim(identifier);
        trim(outputs);

        stringstream outputs_stream(outputs);
        string output_name;
        while (getline(outputs_stream, output_name, ',')) {
            trim(output_name);

            if (condition_flip_or_broadcast == '%') {
                all_outputs[identifier].push_back(output_name);
            }
            else if (condition_flip_or_broadcast == '&') {
                all_outputs[identifier].push_back(output_name);
                conditionals.emplace(identifier);
            } 
            else {
                my_queue.push_back(make_tuple(string("broadcaster"), output_name, 0));
            }
        }
    }


    unordered_map<string, int> string_to_int {{ string("broadcaster"), 0 }};
    unordered_map<int, string> int_to_string {{ 0, string("broadcaster") }};
    int unseen_int = 1;

    for (auto& key_value_pair: all_outputs) {
        if (!in(string_to_int, key_value_pair.first)) {
            string_to_int[key_value_pair.first] = unseen_int;
            int_to_string[unseen_int] = key_value_pair.first;
            unseen_int++;
        }

        for (auto& output_name: key_value_pair.second) {
            if (!in(string_to_int, output_name)) {
                string_to_int[output_name] = unseen_int;
                int_to_string[unseen_int] = output_name;
                unseen_int++;
            }
        }
    }

    vector<bool> is_flip_flop(unseen_int, true);
    for (auto& name: conditionals) {
        is_flip_flop[string_to_int[name]] = false;
    }

    // deque<bfs_node> my_queue_init;
    deque<tuple<int, int, int>> my_queue_init;
    // veque::veque<tuple<int, int, int>> my_queue_init;

    for (auto& the_tuple: my_queue) {
        my_queue_init.push_back(make_tuple(string_to_int[get<0>(the_tuple)], string_to_int[get<1>(the_tuple)], get<2>(the_tuple)));
        // my_queue_init.push_back({
        //     .from_name = string_to_int[get<0>(the_tuple)],
        //     .name = string_to_int[get<1>(the_tuple)],
        //     .signal = get<2>(the_tuple)
        // });
    }


    vector<vector<int>> all_output_ints(unseen_int, vector<int>());
    for (auto& key_value_pair: all_outputs) {
        int num = string_to_int[key_value_pair.first];
        for (auto& key_value_pair_2: key_value_pair.second) {
            all_output_ints[num].push_back(string_to_int[key_value_pair_2]);        
        }
    }

    vector<int> memory_flips(unseen_int, 0);
    vector<vector<int>> memory_conditionals(unseen_int, vector<int>(unseen_int, 1));
    for (auto& key_value_pair: all_outputs) {
        for (auto& output_name: key_value_pair.second) {
            if (in(conditionals, output_name)) {
                int index_1 = string_to_int[output_name];
                int index_2 = string_to_int[key_value_pair.first];
                memory_conditionals[index_1][index_2] = 0;
            }
        }
    }

    int64_t pressed = 1;
    int rx_num = string_to_int["rx"];

    auto start = high_resolution_clock::now();

    while (true) {
        int low_rx_pulses = 0;

        veque::veque<tuple<int, int, int>> iter_queue {
            make_tuple(0, 25, 0),
            make_tuple(0, 49, 0),
            make_tuple(0, 47, 0),
            make_tuple(0, 21, 0),
        };
        iter_queue.reserve(39);

        if (pressed % 1000000 == 0 && pressed != 0) {
            auto interim_time = high_resolution_clock::now();
            auto interim_duration = duration_cast<milliseconds>(interim_time - start);
            auto rate = (double) pressed / (interim_duration.count() / 1000.0f);
            cout << pressed << ", " << rate << " iterations/second. " << pressed << " pressed." << endl;
        }

        while (!iter_queue.empty()) {
            auto [from_name, name, signal] = iter_queue.front();

            iter_queue.pop_front();
            if (name == rx_num && signal == 0) {
                low_rx_pulses += 1;
            }

            if (is_flip_flop[name]) {
                if (signal == 1) {
                    continue;
                }
                memory_flips[name] = 1 - memory_flips[name];
                for (auto sub_name: all_output_ints[name]) {
                    iter_queue.push_back(make_tuple(name, sub_name, memory_flips[name]));
                }
            }
            else {
                memory_conditionals[name][from_name] = signal;
                int to_send_signal = 0;
                for (auto ele: memory_conditionals[name]) {
                    if (ele == 0) {
                        to_send_signal = 1;
                        break;
                    }
                }

                for (auto sub_name: all_output_ints[name]) {
                    iter_queue.push_back(make_tuple(name, sub_name, to_send_signal));
                }
            }
        }

        if (low_rx_pulses == 1) {
            cout << "Took " << pressed << " presses, broke due to 1 low signal rx pulse" << endl;
            break;
        }
        pressed += 1;
    }

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(end - start);
    cout << endl << duration.count() << " seconds taken" << endl;
    return 0;
}
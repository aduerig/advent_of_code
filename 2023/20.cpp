// g++ 20.cpp -std=c++20 -Ofast -o out && ./out

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <chrono>
#include <unordered_map>
#include <deque>
#include <string>
#include <stdint.h>

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


int main() {
    ifstream file("20.dat");
    string line;

    unordered_map<string, vector<string>> flips;
    unordered_map<string, vector<string>> conditional_outputs;

    deque<tuple<string, string, int>> my_queue;
    ;
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
                flips[identifier].push_back(output_name);
            }
            else if (condition_flip_or_broadcast == '&') {
                conditional_outputs[identifier].push_back(output_name);
            } 
            else {
                my_queue.push_back(make_tuple(string("broadcaster"), output_name, 0));
            }
        }
    }

    unordered_map<string, int> memory_flips;
    unordered_map<string, unordered_map<string, int>> memory_conditionals;

    for (auto& key_value_pair: flips) {
        memory_flips[key_value_pair.first] = 0;
    }

    // cout << "conditional outputs: ";
    // for (auto& key_value_pair: conditional_outputs) {
    //     cout << ", " << key_value_pair.first;
    // }
    // cout << endl;

    for (auto& key_value_pair: flips) {
        for (auto& output_name: key_value_pair.second) {
            if (in(conditional_outputs, output_name)) {
                memory_conditionals[output_name][key_value_pair.first] = 0;
            }
        }
    }

    for (auto& key_value_pair: conditional_outputs) {
        for (auto& output_name: key_value_pair.second) {
            if (in(conditional_outputs, output_name)) {
                memory_conditionals[output_name][key_value_pair.first] = 0;
            }
        }
    }

    // cout << "===== Memory =====" << endl;
    // for (auto& key_value_pair: memory_flips) {
    //     cout << "Flip: " << key_value_pair.first << ", " << key_value_pair.second << endl;
    // }

    // for (auto& key_value_pair_1: memory_conditionals) {
    //     cout << "Conditional " << key_value_pair_1.first << ": ";
    //     for (auto& key_value_pair_2: key_value_pair_1.second) {
    //         cout << ", {" << key_value_pair_2.first << ", " << key_value_pair_2.second << "}";
    //     }
    //     cout << endl;
    // }

    int64_t pressed = 1;
    int64_t lows = 0;
    int64_t highs = 0;

    auto start = high_resolution_clock::now();

    // while (pressed < 1001) {
    while (true) {
        int low_rx_pulses = 0;
        deque<tuple<string, string, int>> iter_queue = my_queue;

        if (pressed % 1000000 == 0 && pressed != 0) {
            auto interim_time = high_resolution_clock::now();
            auto interim_duration = duration_cast<milliseconds>(interim_time - start);
            auto rate = (double) pressed / (interim_duration.count() / 1000.0f);
            cout << pressed << ", " << rate << " iterations/second. " << pressed << " pressed." << endl;
        }

        lows += 1;
        while (!iter_queue.empty()) {
            auto&[from_name, name, signal] = iter_queue.front();
            iter_queue.pop_front();

            if (signal == 0) {
                lows += 1;
            } else {
                highs += 1;
            }

            if (name == "rx" && signal == 0) {
                low_rx_pulses += 1;
            }

            if (in(flips, name)) {
                if (signal == 1) {
                    continue;
                }
                memory_flips[name] = 1 - memory_flips[name];
                for (auto& sub_name: flips[name]) {
                    iter_queue.push_back(make_tuple(name, sub_name, memory_flips[name]));
                }
            }
            else if (in(conditional_outputs, name)) {
                memory_conditionals[name][from_name] = signal;
                int to_send_signal = 0;
                for (auto& key_value_pair: memory_conditionals[name]) {
                    if (key_value_pair.second == 0) {
                        to_send_signal = 1;
                        break;
                    }
                }

                for (auto& sub_name: conditional_outputs[name]) {
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
    cout << duration.count() << " seconds taken" << endl;
    cout << "low * high: " << lows * highs << endl;
    return 0;
}
#include <algorithm>
#include <chrono>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

// Namespaces
using namespace std;
namespace fs = std::filesystem;

// ---------------------------------------------------------
// Custom Hash for std::vector
// ---------------------------------------------------------
struct VectorHash {
    size_t operator()(const std::vector<int>& v) const {
        size_t seed = 0;
        for (int i : v) {
            seed ^= std::hash<int>{}(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

// Memoization: Memo[i] stores states known to be unsolvable starting from button index i
using Memo = vector<unordered_set<vector<int>, VectorHash>>;

struct Machine {
    string indic;
    vector<vector<int>> all_buttons;
    vector<int> jolts;
};

// Helper for splitting strings
vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// ---------------------------------------------------------
// Optimized Recursive Solver (DFS on Button Counts)
// ---------------------------------------------------------
bool solve_recursive(int btn_idx, vector<int>& current_jolts,
                     const vector<vector<int>>& all_buttons, long long& total_presses, Memo& memo) {
    // 1. Check if Solved (All zeros)
    bool all_zero = true;
    for (int x : current_jolts) {
        if (x != 0) {
            all_zero = false;
            break;
        }
    }
    if (all_zero) return true;

    // 2. Base Case: No more buttons to try
    if (btn_idx >= all_buttons.size()) return false;

    // 3. Check Memoization (Have we failed here before?)
    if (memo[btn_idx].count(current_jolts)) return false;

    // 4. Determine Max Presses for this button
    // The max presses is limited by the smallest value in the target slots this button affects.
    // Since buttons decrement indices, we check how many times we can subtract before hitting < 0.
    const vector<int>& btn_indices = all_buttons[btn_idx];
    int max_k = 2147483647;  // INT_MAX

    if (btn_indices.empty()) {
        max_k = 0;  // Useless button
    } else {
        for (int idx : btn_indices) {
            if (current_jolts[idx] == 0) {
                max_k = 0;
                break;
            }
            max_k = min(max_k, current_jolts[idx]);
        }
    }

    // 5. Branch and Bound: Try pressing this button k times (Greedy: Max to 0)
    // Applying the max first optimizes for the "Sort by Size" heuristic

    // Optimization: Apply max_k subtractions immediately
    for (int idx : btn_indices) current_jolts[idx] -= max_k;
    total_presses += max_k;

    for (int k = max_k; k >= 0; --k) {
        // Recurse to next button type
        if (solve_recursive(btn_idx + 1, current_jolts, all_buttons, total_presses, memo)) {
            return true;
        }

        // Backtrack: Reduce count by 1 for the next iteration (k-1)
        // If we are at k, the next loop is k-1. We need to "give back" 1 press worth of values.
        if (k > 0) {
            for (int idx : btn_indices) current_jolts[idx]++;
            total_presses--;
        }
    }

    // If we exit the loop, no solution was found from this state
    // Note: The loop ends with k=0 and state fully restored (because we added back 1 each time)
    // so current_jolts is back to its original state at start of function.
    memo[btn_idx].insert(current_jolts);
    return false;
}

long long solve_machine(vector<int> needed_jolt, vector<vector<int>> all_buttons) {
    // Sort buttons by size (greedy heuristic: larger buttons first usually finds solution faster)
    sort(all_buttons.begin(), all_buttons.end(),
         [](const vector<int>& a, const vector<int>& b) { return a.size() > b.size(); });

    // Initialize Memoization table (one set per button index)
    Memo memo(all_buttons.size());

    long long total_presses = 0;
    if (solve_recursive(0, needed_jolt, all_buttons, total_presses, memo)) {
        return total_presses;
    }
    return 0;  // Return 0 if unsolvable (or handle as needed)
}

int main() {
    fs::path source_path = __FILE__;
    fs::path data_file = source_path.parent_path() / "10.dat";

    ifstream file(data_file);
    if (!file.is_open()) {
        file.open("10.dat");  // Fallback to local dir
        if (!file.is_open()) {
            cerr << "Error: Could not open 10.dat" << endl;
            return 1;
        }
    }

    vector<Machine> machines;
    string line;

    // Parsing Logic (Unchanged)
    while (getline(file, line)) {
        if (line.empty()) continue;

        size_t brace_pos = line.find('{');
        string other_part = line.substr(0, brace_pos);
        string jolts_part = line.substr(brace_pos + 1);

        if (!jolts_part.empty() && jolts_part.back() == '}') jolts_part.pop_back();

        vector<int> jolts;
        vector<string> jolt_strs = split(jolts_part, ',');
        for (const auto& s : jolt_strs)
            if (!s.empty()) jolts.push_back(stoi(s));

        size_t bracket_pos = other_part.find(']');
        string indic_str = other_part.substr(0, bracket_pos);
        string buttons_part = other_part.substr(bracket_pos + 1);

        size_t open_bracket = indic_str.find('[');
        string indic =
            (open_bracket != string::npos) ? indic_str.substr(open_bracket + 1) : indic_str;

        vector<vector<int>> all_buttons;
        size_t start = 0;
        while ((start = buttons_part.find('(', start)) != string::npos) {
            size_t end = buttons_part.find(')', start);
            string content = buttons_part.substr(start + 1, end - start - 1);
            vector<int> btn;
            vector<string> nums = split(content, ',');
            for (const auto& n : nums)
                if (!n.empty()) btn.push_back(stoi(n));
            all_buttons.push_back(btn);
            start = end + 1;
        }
        machines.push_back({indic, all_buttons, jolts});
    }

    // Execution
    long long total_presses = 0;

    for (const auto& m : machines) {
        cout << "indic: [" << m.indic << "], all_buttons: ... , jolts: [";
        for (size_t i = 0; i < m.jolts.size(); ++i)
            cout << m.jolts[i] << (i < m.jolts.size() - 1 ? "," : "");
        cout << "]" << endl;

        auto start = chrono::high_resolution_clock::now();
        long long ans = solve_machine(m.jolts, m.all_buttons);
        auto end = chrono::high_resolution_clock::now();

        chrono::duration<double> elapsed = end - start;
        total_presses += ans;
        printf("Solved with %lld presses in %.4f seconds\n", ans, elapsed.count());
    }

    cout << "Needs " << total_presses << " presses" << endl;
    return 0;
}
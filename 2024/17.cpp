// g++ 17.cpp -std=c++17 -Ofast -o out && ./out

#include <iostream>
#include <chrono>
#include <vector>
#include <array>
#include <iomanip>
#include <locale>

using namespace std;
using namespace chrono;


// real
vector<uint64_t> PROG = {
    2,4,
    1,1,
    7,5,
    4,7,
    1,4,
    0,3,
    5,5,
    3,0
};

tuple<int64_t, size_t> encode(vector<uint64_t> arr) {
    uint64_t e = 0;
    for (size_t i = 0; i < PROG.size(); ++i) {
        e |= uint64_t(PROG[i]) << (i * 3);
    }
    return make_tuple(e, PROG.size());
}

vector<uint64_t> decode(uint64_t encoded, size_t len) {
    vector<uint64_t> decoded;
    for (size_t i = 0; i < len; i++) {
        uint64_t mask = (1ULL << ((i + 1) * 3)) - 1;
        uint64_t extract = mask & encoded;
        uint64_t rel = extract >> (i * 3);
        decoded.push_back(rel);
    }
    return decoded;
}

tuple<int64_t, size_t> PROG_ENCODED_TUPLE = encode(PROG);
int64_t PROG_ENCODED = get<0>(PROG_ENCODED_TUPLE);
size_t PROG_LEN = get<1>(PROG_ENCODED_TUPLE);
vector<uint64_t> PROG_DECODED = decode(PROG_ENCODED, PROG_LEN);


int main() {
    vector<uint16_t> PROG_LOOKUP;
    for (size_t i = 0; i < 16; i++) {
        PROG_LOOKUP.push_back((PROG_ENCODED >> i*3) & 7);
    }

    for (uint64_t i: PROG)
        std::cout << i << ' ';
    std::cout << '\n';
    for (uint64_t i: PROG_DECODED)
        std::cout << i << ' ';
    std::cout << '\n';

    auto start = steady_clock::now();
    uint64_t a = 0;
    uint64_t b = 0;
    uint64_t c = 0;

    for (uint64_t a_val = 0; a_val < UINT64_MAX; a_val++) {
    // for (uint64_t a_val = 0; a_val < 1; a_val++) {
        // a_val = 83503;
        // a_val = 416618;
        if (a_val % 1000000000 == 0 && a_val != 0) {
            auto millis = duration_cast<milliseconds>(steady_clock::now() - start).count();
            // cout << format_commas(a_val) << " iter/s: " << format_commas((a_val * 1000.0) / millis) << '\n';
            cout << a_val << " iter/s: " << (a_val * 1000.0) / millis << '\n';
        }

        // # b = a % 8
        // # b = b ^ 1
        // # c = a / pow(2, b)
        // # b = b ^ c
        // # b = b ^ 4
        // # a = a / pow(2, 3)
        // # final.append(b & 7)
        // # if a == 0: halt
        a = a_val;
        b = 0;
        c = 0;
        // cout << "iter: " << a_val << ", result: ";
        for (int i = 0; i < 16; i++) {
            b = a & 7;
            b = b ^ 1;
            c = (uint64_t) (a / (1ULL << b));
            b = b ^ c;
            b = b ^ 4;
            a = (uint64_t) (a / 8);
            // cout << (b & 7) << ',';
            if ((b & 7) != PROG[i]) {
                break;
            }
            if (a == 0) {
                if (i == 15) {
                    cout << a_val << endl;
                    exit(0);
                }
                break;
            }
        }
    }
}
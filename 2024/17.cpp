// g++ 17.cpp -std=c++17 -Ofast -o out && ./out

#include <iostream>
#include <chrono>
#include <vector>
#include <array>

using namespace std;
using namespace chrono;


// real
vector<uint64_t> PROG = {2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0};

// test 1
// vector<uint64_t> PROG = {0, 3, 5, 4, 3, 0};

// test 2
// vector<uint64_t> PROG = {0,1,5,4,3,0};

constexpr array<uint64_t, 64> POW2 = []() {
    array<uint64_t, 64> t{}; 
    uint64_t v = 1;
    for (int i = 0; i < 64; i++) { 
        t[i] = v; 
        v *= 2;
    }
    return t;
}();

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

// # b = a % 8
// # b = b ^ 1
// # c = a / pow(2, b)
// # b = b ^ c
// # b = b ^ 4
// # a = a / pow(2, 3)
// # final.append(b & 7)
// # if a == 0: halt

bool try_value(uint64_t a_val) {
    uint64_t a = 0;
    uint64_t b = 0;
    uint64_t c = 0;
    uint32_t flen = 0;
    for(int i = 0; i < 16; i++) {
        b = a & 7;
        b = b ^ 1;
        c = (uint64_t) (a / (1ULL << b));
        b = b ^ c;
        b = b ^ 4;
        a = (uint64_t) (a / 8);
        if ((b & 7) != ((PROG_ENCODED >> flen) & 7)) {
            return false;
        }
        flen += 1;
        if (a == 0) {
            return true;
        }
    }
    return false;
}

int main() {
    for (uint64_t i: PROG)
        std::cout << i << ' ';
    std::cout << '\n';
    for (uint64_t i: PROG_DECODED)
        std::cout << i << ' ';
    std::cout << '\n';

    auto start = steady_clock::now();
    uint64_t iters = 0;
    for (uint64_t i = 0; i < UINT64_MAX; i++) {
        if (i % 100000000 == 0 && i != 0) {
            auto millis = duration_cast<milliseconds>(steady_clock::now() - start).count();
            cout << i << " iter/s: " << ((iters * 1000.0) / millis) << '\n';
        }
        if (try_value(i)) {
            break;
        }
        iters++;
    }
}
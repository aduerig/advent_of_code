// g++ 17.cpp -o out && ./out

#include <iostream>
#include <chrono>
#include <vector>
#include <array>
#include <iterator>
#include <algorithm>

using namespace std;
using namespace chrono;


// real
vector<uint64_t> PROG = {2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0};

// test 1
// vector<uint64_t> PROG = {0, 3, 5, 4, 3, 0};

// test 2
// vector<uint64_t> PROG = {0,1,5,4,3,0};

constexpr array<uint64_t, 32> POW2 = []() {
    array<uint64_t, 32> t{}; 
    uint64_t v = 1;
    for (int i = 0; i < 32; ++i) { 
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

bool try_value(uint64_t a_val) {
    uint64_t regs[8] = {0, 1, 2, 3, a_val, 0, 0, 7};
    uint64_t final_encoded = 0;
    uint32_t flen = 0;
    size_t ip = 0;
    while (ip < PROG.size()) {
        uint8_t lit = PROG[ip + 1];
        uint64_t combo = regs[lit];
        switch (PROG[ip]) {
            case 0: 
                regs[4] /= POW2[combo];
                ip += 2; 
                break;
            case 1:
                regs[5] ^= lit;
                ip += 2;
                break;
            case 2: 
                regs[5] = combo & 7;
                ip += 2;
                break;
            case 3: 
                ip = (regs[4] != 0) ? lit : ip + 2;
                break;
            case 4: 
                regs[5] ^= regs[6];
                ip += 2;
                break;
            case 5: 
                final_encoded |= (combo & 7) << flen;
                flen += 3;
                ip += 2;
                break;
            case 7: 
                regs[6] = regs[4] / POW2[combo];
                ip += 2; 
                break;
        }
        if (PROG_ENCODED & (1ULL << flen) - 1 ^ final_encoded) {
            return false;
        }
    }
    return final_encoded == PROG_ENCODED;
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
            cout << "Found: " << i << '\n';
            break;
        }
        iters++;
    }
}
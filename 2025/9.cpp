#include <algorithm>
#include <chrono>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

// Namespace alias for convenience
namespace fs = std::filesystem;

struct Point {
    long long x;
    long long y;
};

int main(int argc, char* argv[]) {
    // 1. Setup paths (equivalent to pathlib logic)
    // Note: argv[0] contains the path to the executable
    fs::path filepath = fs::absolute(argv[0]);
    fs::path data_file = filepath.parent_path() / (filepath.stem().string() + ".dat");

    // 2. Start timer
    auto start_time = std::chrono::high_resolution_clock::now();

    std::vector<Point> points;
    long long min_x = std::numeric_limits<long long>::max();
    long long min_y = std::numeric_limits<long long>::max();

    std::ifstream infile(data_file);
    if (!infile.is_open()) {
        std::cerr << "Error: Could not open file " << data_file << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(infile, line)) {
        if (line.empty()) continue;

        // Parse "x,y"
        std::stringstream ss(line);
        std::string segment;
        std::vector<long long> coords;

        while (std::getline(ss, segment, ',')) {
            coords.push_back(std::stoll(segment));
        }

        if (coords.size() >= 2) {
            long long px = coords[0];
            long long py = coords[1];
            points.push_back({px, py});

            if (px < min_x) min_x = px;
            if (py < min_y) min_y = py;
        }
    }
    infile.close();

    // 3. Normalize coordinates and find max dimensions
    long long max_x = 0;
    long long max_y = 0;

    for (auto& p : points) {
        p.x -= min_x;
        p.y -= min_y;

        if (p.x > max_x) max_x = p.x;
        if (p.y > max_y) max_y = p.y;
    }

    // 4. Create Grid
    std::cout << "Making grid with size: " << (max_x + 1) << " x " << (max_y + 1) << std::endl;

    // We use vector<vector<int>> to mimic Python's list of lists.
    // Note: For very large grids, a 1D vector with index math is usually more performant in C++.
    std::vector<std::vector<int8_t>> grid(max_y + 1, std::vector<int8_t>(max_x + 1, 0));

    // Calculate grid creation time
    auto current_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = current_time - start_time;
    printf("Grid made: %.6f seconds\n", diff.count());

    // 5. Plot points on grid
    for (const auto& p : points) {
        grid[p.y][p.x] = 1;
    }

    // 6. Visit all nodes
    std::cout << "Started visiting all nodes" << std::endl;
    long long ok = 0;

    for (size_t y = 0; y < grid.size(); ++y) {
        std::cout << y << std::endl;
        for (size_t x = 0; x < grid[0].size(); ++x) {
            ok++;
        }
    }

    // 7. End timer
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> total_diff = end_time - start_time;

    printf("visiting all nodes and making grid: %.6f seconds, num nodes: %lld\n",
           total_diff.count(), ok);

    return 0;
}
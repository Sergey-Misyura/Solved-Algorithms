#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

bool check_region(int size, const std::vector<std::vector<int>>& region, int n, int m) {
    for (int row = size; row < n - 2 * size + 1; ++row) {
        for (int col = size * 2 - 1; col < m - size; ++col) {
            if (region[row][col + size] >= size * 3) {
                
                bool build = true;
                
                int build_row = row - size;
                while (build && build_row < row) {
                    if (region[build_row][col] < size) {
                        build = false;
                    }
                    build_row += 1;
                }
                
                build_row = row + 1;
                while (build && build_row < row + size) {
                    if (region[build_row][col + size] < size * 3) {
                        build = false;
                    }
                    build_row += 1;
                }
                
                build_row = row + size;
                while (build && build_row < row + size * 2) {
                    if (region[build_row][col] < size) {
                        build = false;
                    }
                    build_row += 1;
                }
                
                if (build) {
                    return true;
                }
            }
        }
    }
    return false;
}

int binSearchRight(int lf, int rg, bool (*check)(int, const std::vector<std::vector<int>>&, int, int), const std::vector<std::vector<int>>& region, int n, int m) {
    while (lf < rg) {
        int mid = (lf + rg + 1) / 2;
        
        if (check(mid, region, n, m)) {
            lf = mid;
        } else {
            rg = mid - 1;
        }
    }
    return lf;
}

int main() {
    std::ifstream f("input.txt");
    int n, m;
    f >> n >> m;
    std::vector<std::vector<int>> region(n, std::vector<int>(m));
    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        std::string line;
        f >> line;
        region[i][0] = line[0] == '.' ? 0 : 1;
        for (int j = 1; j < m; ++j) {
            region[i][j] = line[j] == '.' ? 0 : region[i][j - 1] + 1;
            max_len = std::max(max_len, region[i][j]);
        }
    }

    int answer = binSearchRight(1, std::min({n, m, max_len}) / 3, check_region, region, n, m);

    std::cout << answer << std::endl;

    return 0;
}



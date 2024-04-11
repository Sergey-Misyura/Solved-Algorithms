#include <iostream>
#include <cmath>

int main() {
    long long n;
    std::cin >> n;
    long long diag = int(std::sqrt(n * 2));
    if (!(diag * (diag + 1) / 2 >= n)) {
        diag += 1;
    }
    if (diag == 1) {
        std::cout << "1/1" << std::endl;
    } else {
        int prev_nums_count = int((diag - 1) * diag / 2);
        int diag_idx = n - prev_nums_count;
        int num = diag, denom = diag;
        if (diag % 2) {
            num = diag_idx;
            denom = diag + 1 - num;
        } else {
            denom = diag_idx;
            num = diag + 1 - denom;
        }
        std::cout << num << '/' << denom << std::endl;
    }
    return 0;
}
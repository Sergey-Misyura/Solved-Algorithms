#include <iostream>
#include <cmath>

long long binSearchRight(long long lf, long long rg, bool (*check)(long long, long long), long long checkparams);
long long ships_len(long long ln);
bool check_target(long long m, long long n);

int main() {
    long long n;
    std::cin >> n;
    if (n == 0) {
        std::cout << 0 << std::endl;
    } else {
        std::cout << binSearchRight(1, long (std::sqrt(n)), check_target, n) << std::endl;
    }
    return 0;
}

long long binSearchRight(long long lf, long long rg, bool (*check)(long long, long long), long long checkparams) {
    while (lf < rg) {
        int mid = (lf + rg + 1) / 2;
        if (check(mid, checkparams)) {
            lf = mid;
        } else {
            rg = mid - 1;
        }
    }
    return lf;
}

long long ships_len(long long ln) {
    if (ln == 0) {
        return 0;
    }
    if (ln == 1) {
        return 1;
    }
    long long total = 0;
    long long cur_count = 0; 
    if (ln % 2 == 1) {
        int mid = ln / 2 + 1;
        long long long_mid = (long long) mid;
        total = long_mid * long_mid;
        total += 2 * (long_mid * ((long_mid - 1) * ((long_mid - 1) + 1) / 2));
        cur_count = ships_len(long_mid - 1);
        if (total < 0 || cur_count < 0) {
            total = - 10000;
        } else {
            total += 2 * cur_count;
        }
    } else {
        int mid = ln / 2;
        long long long_mid = (long long) mid;
        total += 2 * ((long_mid + 1) * (long_mid * (long_mid + 1) / 2));
        cur_count = ships_len(long_mid - 1);
        if (total < 0 || cur_count < 0) {
            total = - 10000;
        } else {
            total += 2 * cur_count;
        }
    }
    if (total < 0) {
        total = - 10000;

    }
    return total;
}

bool check_target(long long m, long long n) {
    long long ships_count = m * (m + 1) / 2;
    bool neg = false; 
    long long result_len;
    result_len = ships_len(m);
    
    if (result_len < 0) {
        return false;
    } else {
        return result_len - 1 <= n - ships_count ;
    }
}


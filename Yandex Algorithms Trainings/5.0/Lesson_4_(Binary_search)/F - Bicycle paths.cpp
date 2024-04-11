#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

bool check_tiles(int width, vector<int>& tile_widths, vector<int>& pref_min_y, vector<int>& pref_max_y, vector<int>& suf_min_y, vector<int>& suf_max_y, int n) {
    int last_in = 0;
    for (int i = 0; i < tile_widths.size(); i++) {
        while (last_in < n - 1 && tile_widths[last_in + 1] <= tile_widths[i] + width - 1) {
            last_in += 1;
        }
        int max_y = 0;
        int min_y = 0;
        if (last_in == n - 1) {
            if (i != 0) {
                min_y = pref_min_y[i];
                max_y = pref_max_y[i];
            } else {
                return true;
            }
        } else if (i != 0) {
            min_y = min(pref_min_y[i], suf_min_y[last_in + 1]);
            max_y = max(pref_max_y[i], suf_max_y[last_in + 1]);

        } else {
            min_y = suf_min_y[last_in + 1];
            max_y = suf_max_y[last_in + 1];
        }
        if (max_y - min_y <= width - 1) {
            return true;
        }
    }
    return false;
}

int binSearchLeft(int lf, int rg, bool (*check)(int, vector<int>&, vector<int>&, vector<int>&, vector<int>&, vector<int>&, int), vector<int>& tile_widths, vector<int>& pref_min_y, vector<int>& pref_max_y, vector<int>& suf_min_y, vector<int>& suf_max_y, int n) {
    while (lf < rg) {
        int mid = (lf + rg) / 2;
        if (check(mid, tile_widths, pref_min_y, pref_max_y, suf_min_y, suf_max_y, n)) {
            rg = mid;
        } else {
            lf = mid + 1;
        }
    }
    return lf;
}

int main() {
    int w, h, n;
    cin >> w >> h >> n;
    
    vector<pair<int, int>> tiles;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        tiles.push_back(make_pair(x, y));
    }
    sort(tiles.begin(), tiles.end());
    
    vector<int> pref_min_y(n + 1, INT_MAX);
    vector<int> pref_max_y(n + 1, INT_MIN);
    vector<int> suf_min_y(n + 1, INT_MAX);
    vector<int> suf_max_y(n + 1, INT_MIN);
    for (int i = 0; i < n; i++) {
        pref_min_y[i + 1] = min(pref_min_y[i], tiles[i].second);
    }
    for (int i = 0; i < n; i++) {
        pref_max_y[i + 1] = max(pref_max_y[i], tiles[i].second);
        
    }
    for (int i = n - 1; i >= 0; i--) {
        suf_min_y[i] = min(suf_min_y[i + 1], tiles[i].second);
        
    }
    for (int i = n - 1; i >= 0; i--) {
        suf_max_y[i] = max(suf_max_y[i + 1], tiles[i].second);
        
    }
    
    vector<int> tile_widths;
    for (int i = 0; i < n; i++) {
        tile_widths.push_back(tiles[i].first);
    }
    
    int answer = binSearchLeft(1, max(w, h), check_tiles, tile_widths, pref_min_y, pref_max_y, suf_min_y, suf_max_y, n);
    cout << answer << endl;
    
    return 0;
}


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, result = 1;
vector<vector<int> > lines, LIS;


int binary_search(int target) {
    int start = 0, end = LIS.size() - 1;

    while (start <= end) {
        int mid = (start + end) / 2;

        if (LIS[mid][1] == target) {
            return mid;
        } else if (LIS[mid][1] > target) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return start;
}


void solve() {
    for (int i = 0; i < N; i++) {
        int LIS_LEN = LIS.size();
        if (LIS[LIS_LEN - 1][1] < lines[i][1]) {
            LIS.push_back(lines[i]);
            result++;
        } else {
            int idx = binary_search(lines[i][1]);
            LIS[idx] = lines[i];
        }
    }
}


int main() {
    cin >> N;
    lines.resize(N, vector<int>(2));
    for (int i = 0; i < N; i++) {
        cin >> lines[i][0] >> lines[i][1];
    }
    sort(lines.begin(), lines.end());

    LIS.push_back(lines[0]);

    solve();
    cout << N - result;

    return 0;
}
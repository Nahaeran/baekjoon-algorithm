#include <iostream>
#include <vector>
using namespace std;
 
int N, dp_i = 0;
vector<int> arr, res;
vector<vector<int> > dp;

int mylower_bound(vector<int>& arr, int key){
    int start = 0;
    int end = arr.size() - 1;
    
    int mid;
    
    while(end > start){
        mid = (start + end) / 2;
        if (key > arr[mid]) {
            start = mid + 1;
        }
        else {
            end = mid;
        }
    }
    return end;
}
 
void solve(){
    int cnt = 1;
    res.push_back(arr[0]);
    dp[dp_i][0] = 0;
    dp[dp_i][1] = arr[0];
    dp_i++;

    for (int i = 1; i < N; i++) {
        if(res.back() < arr[i]) {
            res.push_back(arr[i]);
            cnt++;
            
            dp[dp_i][0] = res.size() - 1;
            dp[dp_i][1] = arr[i];
            dp_i++;
        }
        else {
            int idx = mylower_bound(res, arr[i]);
            res[idx] = arr[i];

            dp[dp_i][0] = idx;
            dp[dp_i][1] = arr[i];
            dp_i++;
        }
    }
    
    cout << cnt << endl;

    vector<int> result(cnt);
    int last_idx = cnt - 1;

    for (int i = dp_i - 1; i > -1; i--) {
        if (dp[i][0] == last_idx) {
            
            result[last_idx] = dp[i][1];
            last_idx--;
        }
    }

    for (int i = 0; i < cnt; i++) {
        cout << result[i] << " ";
    }
}
 
int main(){
    cin >> N;
    arr.resize(N + 1);
    dp.resize(N, vector<int>(2, 0));

    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }
    
    solve();
    
    return 0;
}
#include <iostream>
#include <vector>
using namespace std;
 
int N;
vector<int> arr, res;

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

    for (int i = 1; i < N; i++) {
        if(res.back() < arr[i]) {
            res.push_back(arr[i]);
            cnt++;
        }
        else {
            int idx = mylower_bound(res, arr[i]);
            res[idx] = arr[i];
        }
    }
    
    cout << cnt;
}
 
int main(){
    cin >> N;
    arr.resize(N + 1);
    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }
    
    solve();
    
    return 0;
}
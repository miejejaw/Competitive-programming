#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int n;
    cin >> n;
    vector<int> arr(n);

    int first = 0, second = 0;

    for (auto &num : arr){
        cin>>num;
    }

    for(int i=1; i<n; i++)
        for(int idx=1; idx<n-1; idx++){
            if(arr[idx-1]<arr[idx] && arr[idx]>arr[idx+1])
                swap(arr[idx],arr[idx+1]);
        }
    
    string ans = "YES";
    for(int idx=1; idx<n; idx++){
        if(arr[idx] < arr[idx-1]){
            ans = "NO";
            break;
        }
    }

    cout << ans << endl;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    cin>>T;

    while(T--){
        solve();
    }
    return 0;
}



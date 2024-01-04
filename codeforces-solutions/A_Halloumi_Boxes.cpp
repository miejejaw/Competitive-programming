#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N,k;
    cin >> N >> k;
    vector<int> nums(N);
    for (auto &num : nums)
        cin>>num;
    
    string ans = "YES";
    if(k == 1){
        for(int i=1; i<N; i++){
            if(nums[i] < nums[i-1]){
                ans = "NO";
                break;
            }
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



#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N,K;
    cin >> N;
    vector<int> nums(N);
    for (auto &num : nums)
        cin>>num;
    
    sort(nums.begin(),nums.end());
    cin >> K;
    while(K--){
        int left,right;
        cin >> left >> right;
        int l = lower_bound(nums.begin(),nums.end(),left) - nums.begin();
        int r = upper_bound(nums.begin(),nums.end(),right) - nums.begin();
        cout << r-l << ' ';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    // cin>>T;

    while(T--){
        solve();
    }
    return 0;
}



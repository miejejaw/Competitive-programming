#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;
    vector<int> nums(N);
    for (auto &num : nums)
        cin>>num;
    
    ll cur = 0;
    ll ans = 0;
    for (int i = N-1; i > 0; i--) {
        cur += nums[i];
        if (cur > 0) ans += cur;
    }
    ans += nums[0] + cur;
    cout << ans << '\n';
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



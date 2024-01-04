#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N,x;
    cin >> N >> x;
    vector<int> nums(N);
    for (auto &num : nums)
        cin>>num;
    
    int ans = nums[0];
    for(int i=1; i<N; i++){
        ans = max(ans, nums[i]-nums[i-1]);
    }

    cout << max(ans, (x-nums[N-1]) * 2) << endl;

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



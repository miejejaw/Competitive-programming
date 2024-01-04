#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;
    vector<int> nums(N);
    for (auto &num : nums)
        cin>>num;
 
    ll ans = 0;
    for (int i = N - 2; i >= 0; --i)
    {
        if (nums[i] > nums[i + 1])
        {
            int cur = ceil(nums[i] / (double)nums[i + 1]);
            ans += cur - 1;
            nums[i] = nums[i] / cur;
        }
    }
    cout << ans << "\n";

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



#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    vector<ll> nums;
    set<ll> seen;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        if (seen.find(num) == seen.end()) {
            nums.push_back(num);
            seen.insert(num);
        }
    }

    int ans = 1, total=1, len = nums.size();
    sort(nums.begin(), nums.end());

    for(int l=len-2,r=len-1; l>=0; l--){
        total += nums[l+1]-nums[l];
        while(total > N && l<r){
            total -= nums[r]-nums[r-1];
            r--;
        }
        ans = max(ans, r-l+1);
    }

    cout << ans << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    cin >> T;

    while (T--)
    {
        solve();
    }
    return 0;
}

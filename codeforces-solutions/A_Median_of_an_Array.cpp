#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n;
    cin >> n;
    vector<ll> nums(n);
    for (int i=0; i<n; i++){
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());
    ll median = ceil(n / 2.0) - 1;

    auto r = upper_bound(nums.begin(), nums.end(), nums[median]);
    int count = distance(nums.begin() + median, r);
    cout << count << endl;
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

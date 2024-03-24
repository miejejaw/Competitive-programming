#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    vector<ll> nums(N);
    for (auto &num : nums)
        cin >> num;

    sort(nums.begin(), nums.end());
    ll total = 0;
    for (int i = 1; i < N ; i++)
    {
        total += nums[i] - nums[i-1];
    }
    cout << total << endl;
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

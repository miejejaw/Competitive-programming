#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const ll a = (1 << 31) - 1;

void solve()
{
    ll N;
    cin >> N;
    vector<ll> nums(N);
    for (auto &num : nums)
        cin >> num;

    sort(nums.begin(), nums.end());
    int count = 0;
    for (int l = 0, r = N - 1; l < r;)
    {
        if (nums[l] + nums[r] == a)
        {
            count++;
            r--;
            l++;
        }
        else if (nums[l] + nums[r] > a)
        {
            r--;
        }
        else
        {
            l++;
        }
    }

    cout << N - count * 2 + count << endl;
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

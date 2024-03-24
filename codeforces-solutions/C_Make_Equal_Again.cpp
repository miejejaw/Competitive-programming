#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int N;
    cin >> N;
    vector<int> nums(N);
    for (auto &num : nums)
        cin >> num;

    int l = 1, r = N - 2;
    while (l < N && nums[l] == nums[l - 1])
    {
        l++;
    }

    while (r >= 0 && nums[r] == nums[r + 1])
    {
        r--;
    }

    int res = 0;
    if (nums[l - 1] == nums[r + 1])
        res = r - l + 1;
    else
    {
        res = N - max(l, N - r - 1);
    }

    cout << max(0, res) << endl;
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

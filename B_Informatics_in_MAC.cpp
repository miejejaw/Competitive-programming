#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll n;

int check(vector<ll> nums, int mex, int j)
{
    unordered_set<int> visited;

    for (int i = j; i < n; i++)
    {
        if (nums[i] < mex)
        {
            visited.insert(nums[i]);
        }

        if (visited.size() == mex)
        {
            return i;
        }
    }

    if (visited.size() != mex)
    {
        return -1;
    }

    return n - 1;
}

void solve()
{
    cin >> n;
    vector<ll> nums(n);
    set<ll> visited;

    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        visited.insert(nums[i]);
    }

    int mex = 0;
    for (auto it = visited.begin(); it != visited.end(); it++)
    {
        if (*it == mex)
        {
            mex++;
        }
    }

    int a = check(nums, mex, 0);
    int b = check(nums, mex, a + 1);

    if (a == n - 1 || b == -1)
    {
        cout << -1 << endl;
        return;
    }

    cout << 2 << endl;
    cout << 1 << " " << a+1 << endl;
    cout << a + 2 << " " << n << endl;
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

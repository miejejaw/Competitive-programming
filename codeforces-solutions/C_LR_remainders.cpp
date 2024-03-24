#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n, m, count = 0;
    ll total = 1;
    cin >> n >> m;

    vector<int> nums(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> nums[i];
        if (nums[i] % m == 0)
        {
            count++;
        }
        else
        {
            total = total * (nums[i] % m);
        }
    }

    string temp;
    cin >> temp;

    // cout << temp << endl;
    for (int i = 0, l = 0, r = n - 1; i < temp.length(); i++)
    {
        int res = (count > 0) ? 0 : total % m;
        cout << res << ' ';

        if (temp[i] == 'R')
        {
            if (nums[r] % m == 0 )
                count--;
            else
            {
                total /= nums[r] % m;
            }
            r--;
        }
        else
        {
            if (nums[l] % m == 0)
                count--;
            else
            {
                total /= nums[l] % m;
            }
            l++;
        }
    }
    cout << endl;
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

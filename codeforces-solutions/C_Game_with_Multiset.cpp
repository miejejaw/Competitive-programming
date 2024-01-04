#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
vector<int> nums(30);

bool check(ll v)
{
    ll total = 0;
    for (int l = 0, r = 0; r < 30; r++)
    {
        total += (pow(2, r) * nums[r]);
        while (l < r && v < total)
        {
            total -= (pow(2, l) * nums[l]);
            if (total < v)
            {
                ll temp = v - total;
                ll x = pow(2, l);
                nums[l] = temp / x;
                total += (pow(2, l) * nums[l]);
            }
            else
                l++;
        }

        if (total == v)
            return true;
    }

    return false;
}

void solve()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int t;
        ll v;
        cin >> t >> v;

        if (t == 1)
            nums[v]++;
        else
        {
            string ans = (v == 0 || check(v)) ? "YES" : "NO";
            cout << ans << endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    // cin>>T;

    while (T--)
    {
        solve();
    }
    return 0;
}



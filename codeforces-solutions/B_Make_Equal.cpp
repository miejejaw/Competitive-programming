#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N, total = 0;
    cin >> N;
    vector<ll> nums(N);
    for (auto &num : nums)
    {
        cin >> num;
        total += num;
    }

    ll avg = total / N, prefix = 0;
    for (auto num : nums)
    {

        if (num >= avg)
            prefix += num - avg;
        else
        {
            prefix -= avg - num;
            if (prefix < 0)
            {
                cout << "NO\n";
                return;
            }
        }
    }
    cout << "YES\n";
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

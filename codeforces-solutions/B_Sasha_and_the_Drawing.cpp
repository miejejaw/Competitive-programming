#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n, k, res = 0;
    cin >> n >> k;
    ll temp = n * 2 + 2 * (n - 2);
    if (k <= temp)
    {
        res = k / 2 + k%2;
    }
    else
    {
        res = min(2 * n, 2 * n - 2 + k - temp);
    }
    cout << res << endl;
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

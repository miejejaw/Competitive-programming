#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n, k;
    cin >> n >> k;
    int x = n;
    int p = 1;
    while (x > 0)
    {
        int take = x - x / 2;
        if (k <= take)
        {
            cout << p * (2 * k - 1) << '\n';
            break;
        }
        k -= take;
        p *= 2;
        x /= 2;
    }
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

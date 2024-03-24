#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n;
    cin >> n;

    string x;
    cin >> x;

    int z1 = count(x.begin(), x.end(), '0'), z2 = 0;
    int o1 = n - z1, o2 = 0;

    int i = n;
    double m = n / 2.0;

    if (z2 >= o2 && o1 >= z1)
    {
        i = 0;
    }

    for (auto ch : x)
    {
        z2 += ch == '0';
        o2 += ch == '1';

        z1 -= ch == '0';
        o1 -= ch == '1';

        if (z2 >= o2 && o1 >= z1)
        {
            if (abs(n / 2.0 - (o2 + z2)) < m)
            {
                i = o2 + z2;
                m = abs(n / 2.0 - (o2 + z2));
            }
        }
    }

    cout << i << endl;
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

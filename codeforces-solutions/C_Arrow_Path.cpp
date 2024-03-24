#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n;
    cin >> n;

    string rowa, rowb;
    cin >> rowa >> rowb;

    bool dp[2][n];
    dp[0][0] = true;
    dp[1][1] = true;

    for (int i = 2; i < n; i++)
    {
        dp[0][i] = false;
        dp[1][i] = false;
        if (i % 2 == 0)
        {
            if (rowa[i - 1] == '>' && (dp[0][i - 2] || dp[1][i - 1]))
                dp[0][i] = true;
        }
        else
        {
            if (rowb[i - 1] == '>' && (dp[1][i - 2] || dp[0][i - 1]))
                dp[1][i] = true;
        }
    }

    cout << (dp[1][n - 1] ? "YES\n" : "NO\n");
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

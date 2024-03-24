#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N, M;
    cin >> N >> M;
    cout << N * (int)(M / 2) << endl;
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

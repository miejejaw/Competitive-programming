#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int a, b, c;
    cin >> a >> b >> c;
    int count = a + ceil((b + c) / 3.0);

    if ((b%3 == 1 && c < 2) || (b%3 == 2 && c == 0))
        count = -1;

    cout << count << endl;
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

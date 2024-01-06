#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll a, b;
    cin >> a >> b;

    if((a+b) % 2 == 0)
        cout << "Bob \n";
    else
        cout << "Alice \n";
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

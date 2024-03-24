#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    if (N <= 28)
    {
        cout << 'a' << 'a' << (char)('a' + (N - 3)) << endl;
    }
    else if (N <= 53)
    {
        cout << 'a' << (char)('a' + (N - 28))<< 'z' << endl;
    }
    else
    {
        cout << (char)('a' + (N - 53))<< 'z' << 'z' << endl;
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

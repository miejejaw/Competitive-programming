#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll a, b, m;
    cin >> a >> b >> m;

    ll count = ceil((m+1) / (a*1.00));
    if(a == 1) count = m+1;

    if(b == 1) count += m+1;
    else count += ceil((m+1) / (b*1.00));

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

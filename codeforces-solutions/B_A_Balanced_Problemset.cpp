#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll x, n;
    cin >> x >> n;
    if(x%n == 0){
        cout << x/n;
    }
    cout << ans << endl;
    
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

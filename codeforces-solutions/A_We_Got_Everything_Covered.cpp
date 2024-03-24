#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n ,k;
    cin >> n >> k;

    string res = "";
    string ans = "";

    for(int i=0; i<k; i++){
        res += (char)(i+97);
    }

    for(int j=0; j < n; j++){
        ans += res;
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

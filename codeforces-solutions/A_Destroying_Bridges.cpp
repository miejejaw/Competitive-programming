#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n,k;
    cin >> n>>k;

    int ans = 1;

    if(k >= n-1){
        ans = 1;
    }else{
        ans = n;
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

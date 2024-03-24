#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
bool check(ll x, ll y){
    if(x&1) return false;

    ll a = x/2, b=y*2;
    if(max(a,b) != max(x,y) || min(a,b)!= min(x,y))
        return true;
    return false;
}

void solve()
{
    ll x, y;
    cin >> x >> y;

    if(check(x,y) || check(y,x))
        cout << "Yes\n";
    else
        cout << "No\n";

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

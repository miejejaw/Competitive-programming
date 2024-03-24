#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n, m;
    cin >> n >> m;

    vector<ll> numsa(n);
    for (int i = 0; i < n; i++)
    {
        cin >> numsa[i];
    }

    vector<ll> numsb(n);
    for (int i = 0; i < n; i++)
    {
        cin >> numsb[i];
    }


    for (int i = n - 2; i >= 0; i--)
    {
        numsa[i] += min(numsa[i + 1], numsb[i + 1]);
        numsb[i] += min(numsa[i + 1], numsb[i + 1]);
    }

    ll total = numsa[m-1];
    for(int i = 0; i<m; i++){
        total = min(total,numsa[i]);
    }

    cout << total << endl;
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

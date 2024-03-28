#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int pows[200006];
ll rm = 1000'000'007;
 
void calc()
{
    ll cur = 1;
    for (int i = 1; i <= 200005; ++i)
    {
        cur = (cur * 2) % rm;
        pows[i] = cur;
    }
}

void solve()
{
    ll n, k;
    int64_t total = 0;
    
    cin >> n >> k;
    vector<ll> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        total += nums[i];
    }

    int64_t _max = 0, _min = 0, prefix = 0;

    for (int r = 0; r < n; r++)
    {
        prefix += nums[r];
        _max = max(_max, prefix - _min);
        _min = min(_min, prefix);
    }

    total += _max * (pows[k] - 1);

    if(total < 0){
        total = (-total/rm)*rm + total + rm;
    }
    cout << total  << endl;
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

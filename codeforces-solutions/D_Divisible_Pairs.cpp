#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n, x, y, res = 0;
    cin >> n >> x >> y;

    vector<ll> nums(n);
    map<pair<int, int>, int> hmap;

    for (auto &num : nums)
    {
        cin >> num;
        int a = num % x, b = num % y;
        if(a == 0){
            res += hmap[make_pair(0, b)];
            res += hmap[make_pair(0, b + y)];
        }
        res += hmap[make_pair(x-a, b)];
        res += hmap[make_pair(x-a, b + y)];
        hmap[make_pair(num % x, num % y)]++;
    }

    cout << res << endl;
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

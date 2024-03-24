#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    vector<ll> a(N);
    for (auto &num : a)
        cin >> num;

    vector<ll> b(N);
    for (auto &num : b)
        cin >> num;

    vector<pair<ll, ll>> merged;

    for (int i = 0; i < N; ++i)
    {
        merged.push_back({a[i], b[i]});
    }

    sort(merged.begin(), merged.end(), [](const pair<ll, ll> x, const pair<ll, ll> y)
         {
        int x_max = max(x.first, x.second), x_min = min(x.first, x.second);
        int y_max = max(y.first, y.second), y_min = min(y.first, y.second);

        if( x_max>y_max  ||  (x_max == y_max && x_min>y_min))
            return false;
        return true; });

    for (const auto &pair : merged)
    {
        cout << pair.first << ' ';
    }
    cout << endl;

    for (const auto &pair : merged)
    {
        cout << pair.second << ' ';
    }
    cout << endl;
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

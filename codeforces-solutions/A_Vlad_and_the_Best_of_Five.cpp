#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    string temp;
    cin >> temp;

    int x = count(temp.begin(), temp.end(), 'A');
    char ans = (x > temp.length() - x) ? 'A' : 'B';
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

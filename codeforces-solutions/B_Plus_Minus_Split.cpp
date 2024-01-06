#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N, count=0;
    cin >> N;
    
    string chars;
    cin >> chars;

    for (auto &ch : chars){
        count += (ch == '+')? 1 : -1;
    }

     cout << abs(count) << endl;   
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

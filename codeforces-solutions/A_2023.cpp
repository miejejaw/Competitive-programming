#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N, B, total = 1;
    cin >> N >> B;

    while (N--)
    {
        ll num;
        cin >> num;
        total *= num;
    }

    if (2023 % total == 0){
        cout << "YES\n";
        cout << 2023/total;
        B--;
        while(B--){
            cout << " " << 1;
        }
    }
    else
        cout << "NO";
    
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

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n;
    cin >> n;

    if(n%2 == 1){
        cout << "NO\n";
        return;
    }

    cout << "YES\n";

    for(int i=0, f=0; i<n; i+=2){
        if(f)
            cout << "AA";
        else    
            cout << "BB";
        f = !f;
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

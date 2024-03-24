#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    string temp;
    cin >> temp;
    int total = temp[0]=='@';
    for(int i=1; i<N; i++){
        if(temp[i] == temp[i-1] && temp[i] == '*')
            break;
        total += temp[i] == '@';
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

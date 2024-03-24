#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;

    string x;
    cin >> x;

    int count = 0;
    for (int i = 0; i < N - 2;)
    {
        if (x[i] == 'p' && x[i + 1] == 'i' && x[i + 2] == 'e')
        {
            count++;
            i += 3;
        }
        else if (x[i] == 'm' && x[i + 1] == 'a' && x[i + 2] == 'p')
        {
            count++;
            if (i+4<N && x[i+2] == 'p' && x[i + 3] == 'i' && x[i + 4] == 'e')
            {
                i += 2;
            }
            i+= 3;
        }else{
            i++;
        }
    }

    cout << count << endl;
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

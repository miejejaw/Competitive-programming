#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;

    string word;
    cin >> word;

    int first = -1, last = -1;

    for (int index = 0; index < N; index++)
    {
        if (word[index] == 'B')
        {
            if (first == -1){
                first = index;
                last = index;
            }
            else
                last = index;
        }
    }
    cout << last - first + 1 << endl;
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

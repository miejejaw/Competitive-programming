#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int N, neg = 0, zero = 0;
    cin >> N;

    while (N--)
    {
        int num;
        cin >> num;
        neg += (num < 0);
        zero += (num == 0);
    }

    if (neg % 2 == 1 || zero)
    {
        cout << "0\n";
    }
    else
    {
        cout << "1\n";
        cout << "1 0\n";
    }
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

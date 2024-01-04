#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    string num;
    cin >> num;
    int N = num.length(), i = 0;
    int zero = count(num.begin(), num.end(), '0');
    int one = count(num.begin(), num.end(), '1');

    for (; i < N; i++)
    {
        if (num[i] == '0')
        {
            if (one <= 0)
                break;
            one--;
        }
        else
        {
            if (zero <= 0)
                break;
            zero--;
        }
    }

    cout << N - i << endl;
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

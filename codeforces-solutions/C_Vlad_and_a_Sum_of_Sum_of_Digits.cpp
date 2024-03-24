#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const int N = 10E5+1;
ll nums[N];

void solve()
{
    ll N;
    cin >> N;
    cout << nums[N] << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i = 1; i < N; i++)
    {
        int num = i;
        while (num)
        {
            nums[i] += num % 10;
            num /= 10;
        }
        nums[i] += nums[i-1];
    }

    int T = 1;
    cin >> T;

    while (T--)
    {
        solve();
    }
    return 0;
}

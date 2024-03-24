#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int N, flag = 0;
    cin >> N;

    vector<int> nums(N+2);
    for (int i = 0; i < N; i+=2)
    {
        if (flag)
        {
            nums[i] = i + 1;
            nums[i + 1] = i+2;
        }
        else
        {
            nums[i] = i + 2;
            nums[i + 1] = i+1;
        }

        flag = !flag;
    }

    for (int i = 0; i < N; i++)
    {
        cout << nums[i] << " ";
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

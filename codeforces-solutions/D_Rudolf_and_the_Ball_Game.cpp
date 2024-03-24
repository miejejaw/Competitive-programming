#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> nums = {k};

    for (int i = 0; i < m; i++)
    {
        int r;
        cin >> r;
        char c;
        cin >> c;

        set<int> temp;
        for (auto num : nums)
        {
            if (c == '0')
            {
                int x = (r + num > n) ? (r + num) % n : r + num;
                temp.insert(x);
            }
            else if (c == '1')
            {
                int x = (num - r <= 0) ? n  + (num - r) : num - r;
                temp.insert(x);
            }
            else
            {
                int x = (r + num > n) ? (r + num) % n : r + num;
                temp.insert(x);

                x = (num - r <= 0) ? n + (num - r) : num - r;
                temp.insert(x);
            }
        }
        nums = vector<int>(temp.begin(), temp.end());
    }

    cout << nums.size() << endl;

    for (auto num : nums)
    {
        cout << num << ' ';
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

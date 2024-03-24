#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool compare(pair<int, int> &a, pair<int, int> &b)
{
    return a.first > b.first;
}

void solve()
{
    ll N, m;
    cin >> N >> m;
    vector<pair<int, int> > nums;
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        ll num;
        cin >> num;
        int zeros = 0, len = 0;
        bool foundNonZero = false;

        while (num > 0)
        {
            int digit = num % 10;
            num /= 10;

            if (digit != 0)
            {
                foundNonZero = true;
            }

            if (!foundNonZero && digit == 0)
            {
                zeros++;
            }
            len++;
        }
        if (zeros == 0)
            count += len;
        else
            nums.push_back({zeros, len});
    }

    sort(nums.begin(), nums.end(), compare);

    for (int i = 0; i < nums.size(); i++)
    {
        if (i % 2 == 0)
            count += nums[i].second - nums[i].first;
        else
            count += nums[i].second;
    }

    if (count > m)
        cout << "Sasha\n";
    else
        cout << "Anna\n";
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

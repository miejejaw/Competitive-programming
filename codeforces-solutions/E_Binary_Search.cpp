#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int n, x, idx = 0;
    cin >> n >> x;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        if (nums[i] == x)
            idx = i;
    }

    int l = 0, r = n;

    while (r - l > 1)
    {
        int mid = l + (r - l) / 2;
        if (x >= nums[mid])
            l = mid;
        else
            r = mid;
    }


    if (idx == l)
    {
        cout << 0 << endl;
    }
    else
    {
        cout << 1 << endl;
        cout << l+1 << ' ' << idx+1 << endl;
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

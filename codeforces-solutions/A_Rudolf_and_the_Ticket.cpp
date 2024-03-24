#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll n,m,k;
    cin >> n >> m >> k;

    vector<ll> nums1(n);
    for (auto &num : nums1)
        cin >> num;

    vector<ll> nums2(m);
    for (auto &num : nums2)
        cin >> num;
    
    sort(nums2.begin(), nums2.end());

    int count = 0;
    for(int i=0; i<n; i++){
        int x = upper_bound(nums2.begin(), nums2.end(), k-nums1[i]) - nums2.begin();
        count += x;
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

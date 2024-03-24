#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    vector<ll> nums(N*2);
    for (auto &num : nums)
        cin >> num;
    
    sort(nums.begin(), nums.end());
    ll total = 0;
    for(int i=0; i<N*2; i+=2){
        total += nums[i];
    }
    cout << total << endl;
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

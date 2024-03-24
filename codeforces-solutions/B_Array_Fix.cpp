#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll N;
    cin >> N;
    vector<ll> nums(N);
    for (auto &num : nums)
        cin >> num;

    for(int i=N-2,prev=nums[N-1]; i>=0; i--){
        if(nums[i] > prev){
            if(nums[i]%10 > prev || nums[i]/10 > nums[i]%10){
                cout << "NO\n";
                return;
            }

            prev = nums[i]/10;
        }else{
            prev = nums[i];
        }
    }

    cout << "YES\n";
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

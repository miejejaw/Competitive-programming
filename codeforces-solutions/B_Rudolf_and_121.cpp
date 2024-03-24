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

    for(int i=1; i<N-1; i++){
        if(nums[i-1] == 0){
            continue;
        }
        if(nums[i-1] < 0){
            cout << "NO"<< endl;
            return;
        }
        if(nums[i-1] > 0){
            nums[i] -= nums[i-1]*2;
            nums[i+1] -=  nums[i-1];
            nums[i-1] = 0;
        }
    }

    if(nums[N-1] != 0 || nums[N-2] != 0){
        cout << "NO"<< endl;
    }else
        cout << "YES" << endl;
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

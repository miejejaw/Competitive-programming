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
    
    int x = count(nums.begin(), nums.end(), 0);
    vector<int> counts(x, 0);

    string res = "";
    for(int num: nums){
        for(int i=0; i<x; i++){
            if(counts[i] == num){
                counts[i]++;
                res += ('a'+i);
                break;
            }
        }
    }

    cout<< res << endl;
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

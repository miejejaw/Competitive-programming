// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve(){
    int n;
    cin>>n;

    vector<long long> nums(n+1);
    nums.push_back(0);

    for(int i=1; i<=n; ++i){
        cin>>nums[i];
        nums[i] += nums[i-1];
    }

    long long ans = 0;
    for(int i=1; i<n; ++i){
        if(n%i == 0){
            long long _max = 0, _min = -1;
            for(int j=i; j<=n; j += i){
                _max = max(_max,nums[j]-nums[j-i]);
                if(_min == -1 || _min > nums[j]-nums[j-i])
                    _min = nums[j]-nums[j-i];
            }
            ans = max(ans, _max - _min);
        }
    }

    cout<<ans<<endl;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    cin>>T;

    while(T--){
        solve();
    }
    return 0;
}



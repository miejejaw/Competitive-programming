// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void solve(){

    int n;
    cin>>n;

    vector<int> nums(n);

    for(int i=0; i<n; ++i){
        cin>>nums[i];
    }

    int num = *min_element(nums.begin(), nums.end());
    int idx = find(nums.begin(), nums.end(), num) - nums.begin();

    for(int i=idx+1; i<n; i++){
        if(nums[i] < nums[i-1]){
            idx = -1;
            break;
        }
    }

    cout<<idx<<endl;
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



#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N,K;
    cin >> N >> K;
    vector<int> nums(N);
    for (auto &num : nums)
        cin>>num;
    
    while(K--){
        int num;
        cin >> num;
        int idx = upper_bound(nums.begin(),nums.end(),num) - nums.begin();
        cout << idx << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    // cin>>T;

    while(T--){
        solve();
    }
    return 0;
}



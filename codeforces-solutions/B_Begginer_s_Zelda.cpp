#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;
    vector<int> nums(N+1);
    for (int i=1; i<N; i++){
        int a,b;
        cin >> a >> b;
        nums[a]++;
        nums[b]++;
    }

    int ans = 0;
    for(auto num : nums){
        if(num > 2)
          ans += num-2;
    }
    
    cout << ceil(ans/2.0)+1 << endl;
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



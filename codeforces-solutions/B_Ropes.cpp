#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(vector<int>& nums, double x, int k){
   int count = 0;
   for(auto num : nums){
        count += (int) (num/x);
   } 

   return count >= k;
}

void solve(){
    int N, K;
    cin >> N >> K;
    vector<int> nums(N);
    for (auto &num : nums){
        cin>>num;
    }

    double left = 0;
    double right = 10e8;
    for(int i=0; i<100; i++){
        double mid = left + (right-left)/2;
        if(check(nums, mid, K))
            left = mid;
        else
            right = mid;

    }
    
    cout<< setprecision(8) <<left;   
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



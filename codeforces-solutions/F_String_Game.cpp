#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
string t,p;
int N = 0;
vector<int> nums;

bool check(int l){
    string temp = t;
    for(int i=0; i<=l; i++){
        temp[nums[i]-1] = '#';
    }
    // cout << temp << l << endl;
    int idx = 0;
    for(auto ch : p){
        while(idx<N && temp[idx] != ch){
            idx++;
        }

        if(idx >= N) return false;
        idx++;
    }

    return true;
}

void solve(){
    
    cin >> t >> p;
    N = t.length();
    nums.resize(N);

    for (auto &num : nums)
        cin>>num;

    int left = 0, right = N-1;
    while(left < right){
        int mid = left + (right-left)/2;

        if(!check(mid))
            right = mid;
        else
            left = mid+1;
    }

    cout<<left;
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



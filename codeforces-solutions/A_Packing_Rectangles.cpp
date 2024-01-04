#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll w,h,n;

bool check(ll l){
    return (l/w) * (l/h) >= n;
}

void solve(){
    cin >> w >> h >> n;

    ll left = 0, right = 1;
    while(!check(right)){
        right <<= 1;
    }

    while(left < right){
        ll mid = left + (right-left)/2;
        if(check(mid))
            right = mid;
        else
            left = mid + 1;
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



#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll n, x, y;

bool check(ll t){
    ll count = (t/x) + (t/y);
    return n-1 <= count;
}

void solve(){
    cin >> n >> x >> y;
    
    ll left = 0, right = min(x,y)*(n-1);

    while(left < right){
        ll mid = left + (right-left)/2;
        if(check(mid))
            right = mid;
        else
            left = mid+1;
    }

    cout<<left + min(x,y);
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



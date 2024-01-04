#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    ll N, prev = 0, ans = 0;
    cin >> N;

    while (N--){
        int num;
        cin >> num;
        ans += (num-prev > 0)? num-prev : 0;
        prev = num;
    }

    cout << ans-1 << endl;
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


/*
1 2 3 4 5 6 7 8 9

*/
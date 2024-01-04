#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;

    string s;
    cin >> s;

    int count = 0, _max = 0, ans = 0;
    for(int i=0; i<N; i++){
        count += (s[i] == '.');
        ans += (s[i] == '.');
        if(s[i] == '#') count = 0;
        _max = max(_max,count);
    }
    ans = (_max > 2)? 2 : ans;
    cout << ans << endl;
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



#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;
    string s;
    cin >> s;

    int b_count = 0, ans = 0;
    for(int i=N-1; i>=0; i--){
        b_count += (s[i] == 'B');
        if(s[i] == 'A'){
            ans += b_count;
            b_count = (b_count>0);
        }
    }

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



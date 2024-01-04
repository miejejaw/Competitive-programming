#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int check(int x, int a, int b){
    if(abs(a-b)%2 == 0)
        return 1;
    
    return 0;
}

void solve(){
    int a, b, c;
    cin >> a >> b >> c;

    cout << check(a,b,c) << ' ';
    cout << check(b,a,c) << ' ';
    cout << check(c,b,a) << endl;
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



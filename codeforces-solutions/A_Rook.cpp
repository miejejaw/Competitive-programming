#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    string x;
    cin >> x;

    for(char ch ='a'; ch < 'i'; ch++){
        if(x[0] != ch)
            cout << ch << x[1] << endl;
    }

    for(int ch =1; ch < 9; ch++){
        if(x[1]-'0' != ch)
            cout << x[0] << ch << endl;
    }

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



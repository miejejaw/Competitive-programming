#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    string num;
    cin >> num;
    int N = num.length(), i=1;

    for(; i<N; i++){
        if(num[i] != '0')
            break;
    }
    if(i == N){
        cout << -1 << endl;
        return;
    }
    
    int num1 = stoi(num.substr(0,i));
    int num2 = stoi(num.substr(i,N));

    if(num1 >= num2){
        cout << -1 << endl;
        return;
    }

    cout << num1 << ' '<< num2 << endl;

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



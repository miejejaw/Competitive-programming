#include <bits/stdc++.h>

using namespace std;

void solve(){
    int r, c;
    cin>>r>>c;

    int zero = 0, one = 0, two = 0, num;
    cin>>num;
    int first = num;

    do{
        if(num == 0)
            zero++;
        else if(num == 1)
            one++;
        else
            two++;
    }while(cin>>num);

    int res = 0;
    if(zero == 1){
        if(r == 1 || c == 1)
            res = (min(first,num) > 0)? min(first,num) : max(first,num);
        else
            res = (one > 0)? 1 : 2;
    }
    else if(zero == 0 && two%2 == 1){
        res = pow(2,two/2);
    }
     
    cout<<res;
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


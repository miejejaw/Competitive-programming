#include <iostream>

using namespace std;

void solve(){
    int n;
    cin>>n;
    if(n%3 == 0)
        cout<<"Second";
    else
        cout<<"First";
    cout<<endl;
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



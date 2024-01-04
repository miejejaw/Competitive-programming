#include <bits/stdc++.h>

using namespace std;

void solve(){

    int P,N,count=0;
    cin>>P>>N;
    unordered_set<string> visited;

    while(N--){
        string part;
        cin>>part;

        count++;
        visited.insert(part);
        if(visited.size() == P){
            cout<<count;
            return;
        }

        
    }

    cout<<"paradox avoided";
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



#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n,k;
    cin>>n>>k;

    string word;
    cin>>word;

    int b = count(word.begin(), word.end(), 'B');
    int x = abs(k-b), res = 0;
    char ch = ' ';

    if(b < k){
        for(int i=0; i<n; i++){
            x += (word[i] == 'A')? -1 : 0;
            if(x == 0){
                res = i+1;
                ch = 'B';
                break;
            }
        }
    }
    else if(b > k){
        for(int i=0; i<n; i++){
            x += (word[i] == 'B')? -1 : 0;
            if(x == 0){
                res = i+1;
                ch = 'A';
                break;
            }
        }
    }
    
    if(res == 0){
        cout<<0<<endl;
        return;
    }

    cout<<1<<endl;
    cout<<res<<' '<<ch<<endl;
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



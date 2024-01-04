#include <bits/stdc++.h> 

using namespace std;

void solve(){

    int a, b, n =  1299827;
    string p;
    cin>>a>>b;
    cin>>p;

    vector<bool> primes(n + 1, true);
    primes[0] = primes[1] = false; 

    for (int i = 2; i * i <= n; ++i) {
        if (primes[i]) {
            for (int j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }


    int j = 0, count = 0;

    for (int i = 2; i <= n; ++i) {
        if (primes[i] ) {
            j++;
            if (a<=j && j<=b && to_string(i).find(p) != string::npos) {
                count++;
            }
        }
    }


    cout<<count;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;

    while(T--){
        solve();
    }
    return 0;
}



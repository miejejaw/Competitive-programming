// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void solve(){
    int n;
    cin>>n;

    long long res = -100000, total = 0;
    int prev = 2;

    for (int i = 0; i < n; ++i) {
        int num;
        cin >> num;

        if (total < 0 || prev == abs(num%2)) {
            total = 0;
        }

        total += num;   
        res = max(res, total);
        prev = abs(num%2);
    }

    cout<<res<<endl;
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



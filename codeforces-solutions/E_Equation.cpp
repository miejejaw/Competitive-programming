#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(double c , double x){
    return x*x + sqrt(x) >= c;
}

void solve(){
    double c;
    cin >> c;

    double left = 0, right = 100000;

    while(right-left > 0.000001){
        double mid = left + (right-left)/2.0;
        if(check(c, mid))
            right = mid;
        else
            left = mid;
    }

    cout<< setprecision(16) << left;

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



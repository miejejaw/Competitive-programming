#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll m, n;
vector<tuple<int,int,int>> assistants;

bool check(ll x){
    int count = 0;
    for (auto assistant : assistants){
        int tie(t, z, y) = assistant;

        if(t <= x){
            count++;
            

        }
    
    }
}

void solve(){
    cin >> m >> n;

    for (int i=0; i<n; i++){
        int t, z, y;
        cin >> t >> z >> y;
        assistants.push_back(tuple<int,int,int>(t,z,y));
    }

    ll left = 0, right = 1e8;
    while(left < right){
        ll mid = left + (right-left)/2;
        if(check(mid))
            right = mid;
        else
            left = mid+1;
    }

    cout<<left;
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



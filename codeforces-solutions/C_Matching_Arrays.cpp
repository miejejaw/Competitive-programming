#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int n,x;
    cin >> n >> x;
    vector<pair<int,int>> a;
    for (int i=0; i<n; i++){
        int num;
        cin>>num;
        a.push_back(make_pair(num,i));
    }
    
    sort(a.begin(), a.end());
    vector<int> b(n);
    for (auto &num : b)
        cin>>num;
    
    sort(b.begin(), b.end());

    vector<int> res(n);
    int idx = n-x;
    for(int j=0; j<x; j++){
        res[idx] = b[j];
        idx++;
    }

    idx = x;
    for(int j=0; j<n-x; j++){
        res[j] = b[idx];
        idx++;
    }

    int count = 0;
    for(int j=0; j<n; j++){
        if(res[j] < a[j].first)
            count++;
    }

    if(count == x){
        for(int j=0; j<n; j++){
            b[a[j].second] = res[j];
        }

        cout << "YES" << endl;
        for(int j=0; j<n; j++){
            cout << b[j] << ' ';
        }
        cout << endl;
    }
    else
        cout << "NO" << endl;

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



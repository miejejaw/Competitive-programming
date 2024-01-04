#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;

    vector<vector<int>> nums(N, vector<int>(N));
    vector<int> res(N);

    for (int i = 0; i < N; ++i) {
        ll num = 1073741823;
        for (int j = 0; j < N; ++j) {
            cin >> nums[i][j];
            if (j != i)
                num &= nums[i][j];
        }
        res[i] = (num == 1073741823)? 0: num;
    }

    string ans = "YES";
    for (int i = 0; i < N; ++i) {
        for (int j = i+1; j < N; ++j) {
            if (j != i && (res[j] | res[i]) != nums[i][j]) {
                ans = "NO";
                break;
            }
        }
    }

    cout << ans << endl;
    if (ans == "YES") {
        for (auto x : res)
            cout << x << ' ';
        cout << endl;
    }

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



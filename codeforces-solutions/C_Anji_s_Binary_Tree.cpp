#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;

    string path;
    cin >> path;
    unordered_map<int,pair<int,int>> root;
    for (int i=1; i<=N; i++){
        int left, right;
        cin >> left >> right;
        root[i] = make_pair(left,right);
    }

    queue<tuple<int, int>> qq;
    qq.push(make_tuple(1, 0));
    int ans = N;

    while (!qq.empty()) {
        int curr, count;
        tie(curr, count) = qq.front();
        qq.pop();

        if (root[curr].first == 0 && root[curr].second == 0)
            ans = min(ans, count);

        else {
            if(root[curr].first != 0)
                qq.push(make_tuple(root[curr].first, count + (path[curr - 1] != 'L')));

            if(root[curr].second != 0)
                qq.push(make_tuple(root[curr].second, count + (path[curr - 1] != 'R')));
        }
    }

    cout << ans << endl;       
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



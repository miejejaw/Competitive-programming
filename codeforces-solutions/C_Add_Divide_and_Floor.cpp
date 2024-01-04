#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(){
    int N;
    cin >> N;
    vector<ll> nums(N);
    for (auto &num : nums)
        cin >> num;
    
    sort(nums.begin(), nums.end());
	int p = nums[0], q = nums[N-1];
	vector<ll> ans;

	while (p != q) {
		ans.push_back(p % 2);
		int r = p % 2;
		p = (p + r) / 2;
		q = (q + r) / 2;
	}

	cout << ans.size() << endl;
	if (ans.size() != 0 && ans.size() <= N) {
		for (auto x: ans) 
            cout << x << ' ';
        cout << endl;
	}

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    cin >> T;

    while(T--){
        solve();
    }
    return 0;
}



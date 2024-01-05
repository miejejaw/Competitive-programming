#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    ll A, B, ans;
	cin >> A >> B;
    
	if(B % A == 0){
		ans = B * (B / A);
	} else {
		ans = A / __gcd(A, B) *B;
	}

	cout << ans << '\n';
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    cin >> T;

    while (T--)
    {
        solve();
    }
    return 0;
}

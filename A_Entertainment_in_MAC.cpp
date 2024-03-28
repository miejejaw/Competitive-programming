#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(string temp){
    int l = 0, r = temp.length() - 1;
    while(l < r){
        if(temp[l] < temp[r])
            return true;
        else if(temp[l] > temp[r])
            return false;
        l++;
        r--;
    }
    return true;
}

void solve()
{
    ll n;
    cin >> n;

    string temp;
    cin >> temp;


    if (check(temp))
        cout << temp << endl;
    else
    {
        string a = temp;
        reverse(temp.begin(), temp.end());
        cout << temp << a << endl;
    }

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

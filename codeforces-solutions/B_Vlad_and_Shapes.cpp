#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int N, first = -1, last = 0;
    cin >> N;
    
    for (int i=0; i<N; i++){
        string temp;
        cin >>temp;
        int x = count(temp.begin(), temp.end(), '1');
        if(x>0){
        if(first == -1) first = x;
        last = x;
        }
    }

    if(last == first){
        cout << "SQUARE\n";
    }else{
        cout << "TRIANGLE\n";
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

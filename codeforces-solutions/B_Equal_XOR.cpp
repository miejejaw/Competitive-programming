#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int N, k;
    cin >> N >> k;
    k*=2;

    vector<int> numsa(N);
    unordered_set<int> vs;
    for (auto &num : numsa)
    {
        cin >> num;
        vs.insert(num);
    }

    vector<int> numsb(N);
    for (auto &num : numsb)
        cin >> num;

    sort(numsa.begin(), numsa.end());
    sort(numsb.begin(), numsb.end());
    int du = (k/2 < N-vs.size()) ? k/2 : N-vs.size();
    int nd = k - 2*du;

    for (int i = 1, j=du; i <N; i++)
    {
        if(j && numsa[i] == numsa[i-1]){
            cout << numsa[i] << ' ' << numsa[i] << ' ';
            j--;
        }
    }

    for (int i = 0, j=nd; i <N; i++)
    {
        if(i+1<N && numsa[i] == numsa[i+1]){
            i++;
        }
        else if(j > 0){
            cout << numsa[i] << ' ';
            j--;
        }
        
    }
    cout << endl;

    for (int i = 1, j=du; i <N; i++)
    {
        if(j && numsb[i] == numsb[i-1]){
            cout << numsb[i] << ' ' << numsb[i-1] << ' ';
            j--;
        }
    }

    for (int i = 0, j=nd; i <N; i++)
    {
        if(i+1<N && numsb[i] == numsb[i+1]){
            i++;
        }
        else if(j>0){
            cout << numsb[i] << ' ';
            j--;
        }
        
    }
    cout << endl;


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

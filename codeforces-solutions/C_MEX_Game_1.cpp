#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(int number, const set<int>& mySet) {
    auto it = mySet.find(number);
    return it != mySet.end();
}

void solve()
{
    int N;
    cin >> N;

    set<int> numsa, numsb;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;

        if(!check(num, numsa) && !check(num,numsb)){
            numsb.insert(num);
        }else if(check(num,numsb)){
            numsa.insert(num);
            numsb.erase(num);
        }
    }


    int f=1;

    for (auto it = numsb.begin(); it != numsb.end(); ++it)
    {
        if (f)
        {
            numsa.insert(*it);
        }

        f = !f;
    }

    int prev = 0;

    for (auto it = numsa.begin(); it != numsa.end(); ++it)
    {
        if(*it > prev){
            break;
        }
        
        prev++;
    }

    cout << prev << endl;
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

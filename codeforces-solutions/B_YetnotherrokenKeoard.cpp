#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    string temp;
    cin >> temp;
    int N = temp.length();
    stack<int> capital;
    stack<int> small;

    for (int i=0; i<N; i++)
    {
        if(isupper(temp[i])){
            if (!capital.empty() && temp[i] == 'B')
                capital.pop();
            else if (temp[i] != 'B')
            {
                capital.push(i);
            }
        }
        else{
            if (!small.empty() && temp[i] == 'b')
                small.pop();
            else if (temp[i] != 'b')
            {
                small.push(i);
            }
        }
    }

    vector<int> res;
    while(!capital.empty()){
        res.push_back(capital.top());
        capital.pop();
    }

    while(!small.empty()){
        res.push_back(small.top());
        small.pop();
    }

    sort(res.begin(), res.end());
    for(auto i: res)
    {
        cout << temp[i];
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

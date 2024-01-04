#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
    int N;
    cin >> N;
    string temp;
    cin >> temp;
    
    stack<char> st;
    for (auto ch : temp)
    {
        while (!st.empty() && ch == st.top())
        {
            char a = st.top();
            st.pop();
    
            if(st.empty() || a == st.top()){
                st.push(a);
                break;
            }
            st.pop();
        }

        if (!st.empty() && st.top() != ch)
        {
            char a = st.top();
            st.pop();
            if (st.empty() || st.top() != a)
            {
                st.push(a);
                st.push(ch);
            }
        }
        else
        {
            st.push(ch);
        }
    }


    int ans = 0;
    while (!st.empty()) {
        char a = st.top();
        st.pop();

        if (!st.empty() && a != st.top()) {
            st.pop();
        }else
            ans++;

    }
    
    cout << ans << endl;
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


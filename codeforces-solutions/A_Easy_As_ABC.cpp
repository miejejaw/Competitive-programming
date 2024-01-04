#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef long long ll;
char grid[3][3];
vector<pair<int, int>> dir = {{0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}};
bool inbound(int x, int y)
{
    return x >= 0 && x < 3 && y >= 0 && y < 3;
}

string bfs(int sx, int sy)
{
    queue<tuple<int, int, string>> qq;
    set<pair<int, int>> visited;
    qq.push(make_tuple(sx, sy, string(1, grid[sx][sy])));
    string res = "CCC";

    while (!qq.empty())
    {
        int x, y;
        string temp;
        tie(x, y, temp) = qq.front();
        qq.pop();
        visited.insert(make_pair(x, y));
        if (temp.length() == 3)
        {
            if (res > temp)
            {
                res = temp;
                continue;
            }
        }

        for (auto dd : dir)
        {
            int i = dd.first + x;
            int j = dd.second + y;
            if (inbound(i, j) && visited.find(make_pair(i, j)) == visited.end())
            {
                qq.push(make_tuple(i, j, temp + grid[i][j]));
            }
        }
    }

    return res;
}

void solve()
{

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> grid[i][j];
        }
    }

    string ans = "CCC";
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            string temp = bfs(i, j);
            if (ans > temp)
                ans = temp;
        }
    }

    cout << ans << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    // cin>>T;

    while (T--)
    {
        solve();
    }
    return 0;
}

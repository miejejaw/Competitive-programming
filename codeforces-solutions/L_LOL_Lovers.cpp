#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve()
{
    int N;
    cin >> N;

    string foods;
    cin >> foods;

    int b = 0, o = 0;
    int countB = count(foods.begin(), foods.end(), 'L');
    int countO = count(foods.begin(), foods.end(), 'O');

    for (auto food : foods)
    {
        if (food == 'O')
        {
            o++;
            countO--;
        }
        else
        {
            b++;
            countB--;
        }

        if (b != countB && o != countO && (countB != 0 || countO != 0))
            return b + o;
    }

    return -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    // cin>>T;

    while (T--)
    {
        cout << solve();
    }
    return 0;
}

#include<iostream>
#include<string>
#include<cctype>
#include<algorithm>
#include<set>
#include<unordered_map>
#include<map>
#include<cmath>
#include<bitset>
#include<utility>
#include<set>
#include<vector>
#include <iomanip> 

using namespace std;

void solve(){

    int k;
    char my_ans[1001],friend_ans[1001];

    scanf("%d", &k);
    scanf(" %1000[^\n]", my_ans);
    scanf(" %1000[^\n]", friend_ans);

    int length = 0,right=0;

    for(int idx=0; my_ans[idx] != '\0'; idx++){
        if(my_ans[idx] == friend_ans[idx])
            right++;
        
        length++;
    }

    printf("%d", min(right,k)+(length-right)-max(0,k-right));


}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T = 1;
    // cin>>T;

    while(T--){
        solve();
    }
    return 0;
}



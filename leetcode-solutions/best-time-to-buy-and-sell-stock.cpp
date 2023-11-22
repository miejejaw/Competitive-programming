class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int min_price = 1e5, ans = 0;
        for(auto price : prices){
            ans = max(ans, price - min_price);
            min_price = min(min_price,price);
        }

        return ans;
    }
};
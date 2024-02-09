class Solution {
public:
    bool canPartition(vector<int>& nums) {

        int sum = accumulate(begin(nums), end(nums), 0);
        if(sum % 2 != 0) return false;

        int target = sum / 2;

        vector<bool> dp(target + 1, false);
        dp[0] = true;
        
        for (int num : nums) {
            for (int i = target; i >= num; --i) {
                dp[i] = dp[i] || dp[i - num];
            }
        }

        return dp[target];
    }
};

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

        vector<int> res;
        int ans = 1;

        for (int num : nums) {
            int idx = lower_bound(res.begin(),res.end(),num) - res.begin();
            ans = max(ans, idx+1);

            if(idx < res.size())
                res[idx] = num;
            else
                res.push_back(num);
        }

        return ans;
    }
};
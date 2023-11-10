class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int length = nums.size();
        std::vector<pair<int,int>> res(length, make_pair(1,1));
        int ans = 1, pairs = 0;

        for (int i = 0; i < length; ++i) {
            int count = 0, len = 0;
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    if(len < res[j].first){
                        len = res[j].first;
                        count = res[j].second;
                    }
                    else if(len == res[j].first)
                        count += res[j].second;
                }
            }

            res[i].first += len;
            res[i].second = count>1 ? count : 1;

            if(ans < res[i].first){
                ans = res[i].first;
                pairs = res[i].second;
            }
            else if(ans == res[i].first)
                pairs += res[i].second;
        }

        return pairs;
    }
};
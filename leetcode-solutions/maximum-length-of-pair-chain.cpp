class Solution {
public:
    static bool cmp(const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0])
            return a[1] > b[1];
        return a[0] < b[0];
    }

    int findLongestChain(vector<vector<int>>& pairs) {

        int length = pairs.size();
        if (length == 0) return 0;
        sort(pairs.begin(), pairs.end(), cmp);

        vector<int> ans;
        ans.push_back(pairs[0][1]);

        for(int i=1; i<length; i++){
            if(pairs[i][0] > ans.back())
                ans.push_back(pairs[i][1]);
            else if(pairs[i][1] < ans.back()){
                auto it = lower_bound(ans.begin(),ans.end(),pairs[i][0]);
                *it = pairs[i][1];
            }
        }
        return ans.size();
    }
};
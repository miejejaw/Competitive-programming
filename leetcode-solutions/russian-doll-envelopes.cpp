class Solution {
public:
    static bool cmp(const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0])
            return a[1] > b[1];
        return a[0] < b[0];
    }

    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int length = envelopes.size();
        if (length == 0) return 0;
        sort(envelopes.begin(), envelopes.end(), cmp);

        vector<int> ans;
        ans.push_back(envelopes[0][1]);

        for(int i=1; i<length; i++){
            if(envelopes[i][1]>ans.back())
                ans.push_back(envelopes[i][1]);
            else{
                auto it = lower_bound(ans.begin(),ans.end(),envelopes[i][1]);
                *it = envelopes[i][1];
            }
        }
        return ans.size();
    }
};


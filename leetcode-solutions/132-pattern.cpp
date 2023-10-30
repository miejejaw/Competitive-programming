class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> st;
        int min_num = -1000000001;

        for(int idx=nums.size()-1; idx>=0; idx--){
            while(!st.empty() && st.top() < nums[idx]){
                min_num = max(min_num,st.top());
                st.pop();
            }

            if(min_num > nums[idx])
                return true;
            
            st.push(nums[idx]);
        }

        return false;
    }
};
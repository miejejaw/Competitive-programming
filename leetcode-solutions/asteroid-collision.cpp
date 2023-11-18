class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;
        for(int num : asteroids){
            if(num < 0){
                while(!st.empty() && abs(num) > st.top() && st.top() > 0){
                    st.pop();
                }

                if(!st.empty() && abs(num) == st.top())
                    st.pop();
                else if(st.empty() || st.top()<0)
                    st.push(num);
            }
            else{
                st.push(num);
            }
        }

        vector<int> res(st.size());
        for(int i = st.size()-1; i >= 0; i--) {
            res[i] = st.top();
            st.pop();
        }

        return res;
    }
};
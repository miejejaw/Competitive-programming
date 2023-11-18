class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> res;
        for(int num : asteroids){
            if(num < 0){
                while(!res.empty() && -num > res.back() && res.back() > 0){
                    res.pop_back();
                }

                if(!res.empty() && -num == res.back())
                    res.pop_back();
                else if(res.empty() || res.back()<0)
                    res.push_back(num);
            }
            else{
                res.push_back(num);
            }
        }

        return res;
    }
};
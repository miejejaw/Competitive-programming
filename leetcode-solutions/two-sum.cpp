class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int length = nums.size();
        map<int,int> hmap;

        for(int i=0; i<length; i++){
            if(hmap.count(target-nums[i]) == 1){
                return {i,hmap[target-nums[i]]};
            }
            hmap[nums[i]] = i;
        }

        return {-1,-1};
    }
};
class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int length = nums.size();
        int left=0,right=length-1;

        while(left<right){
            int mid = left + (right-left)/2;
            if(nums[mid] <= nums[right])
                right = mid;
            else
                left = mid+1;
        }

        int peak = left, ans = -1;

        if(target < nums[0] || peak == 0){
            int idx = lower_bound(nums.begin()+peak, nums.end(),target) - nums.begin();
            if(idx >= peak && idx < length && nums[idx] == target)
                ans = idx;
        }else{
            int idx = lower_bound(nums.begin(), nums.begin()+peak,target) - nums.begin();
            if(idx < peak && idx >= 0 && nums[idx] == target)
                ans = idx;
        }

        return ans;
    }
};
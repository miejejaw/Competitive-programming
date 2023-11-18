class Solution {
public:
    int findPeakElement(vector<int>& nums) {

        int left = 0;
        int right = nums.size() - 2;

        while (left < right) {
            int mid = left + (right - left) / 2;
 
            if(nums[mid] < nums[mid+1]) {
                left = mid+1; 
            } else {
                right = mid; 
            }
        }

        if(nums.size() != 1 && nums[left] < nums[left+1])
            left++;
        
        return left;
    }
};
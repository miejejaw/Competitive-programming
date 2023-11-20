class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        
        maxSum -= n;
        long l = index, r = n-index-1;
        long left = 0, right = maxSum, ans = 0;

        while(left <= right){
            long mid = left + (right-left)/2;
            long long total = mid;
            int ll = min(l,mid-1);
            int rr = min(r,mid-1);
            total += (ll*(mid-ll+mid-1)) / 2;
            total += (rr*(mid-rr+mid-1)) / 2;

            if(total <= maxSum){
                left = mid+1;
                ans = mid;
            }
            else
                right = mid-1;

        }

        return ans+1;

    }
};


















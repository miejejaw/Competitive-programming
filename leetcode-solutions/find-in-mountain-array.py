class Solution:
    def findInMountainArray(self, target: int, mountain_arr) -> int:
        length = mountain_arr.length()
        beg,end = 0,length-1

        while beg<end:
            mid = beg + (end-beg)//2
            num = mountain_arr.get(mid)
            left = mountain_arr.get(mid-1)
            right = mountain_arr.get(mid+1)
            if left < num and num > right:
                beg = mid 
                break
            elif left > num > right:
                end = mid
            else:
                beg = mid+1
        
        if mountain_arr.get(beg) < target: return -1

        left,right = 0,beg
        while left < right:
            mid = left + (right-left)//2
            num = mountain_arr.get(mid)
            if num == target: return mid
            if num > target:
                right = mid
            else:
                left = mid+1
        
        if mountain_arr.get(left) == target: return left

        left,right = beg,length-1
        while left < right:
            mid = left + (right-left)//2
            num = mountain_arr.get(mid)
            if num == target: return mid
            if num < target:
                right = mid
            else:
                left = mid+1
        
        if mountain_arr.get(left) == target: return left
        return -1

from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,k = IL()
nums = IL()


def countWiner(nums,k,):
    length = len(nums) 
    res = mergeSort(nums,0,length-1)
    ans = []
    for num,ind in res:
        ans.append(ind)
    return ans
    
def mergeSort(nums,left,right):
    if left == right:
        return [(nums[left],left+1)]
    
    mid = left + (right-left)//2
    leftArr = mergeSort(nums,left,mid)
    rightArr = mergeSort(nums,mid+1,right)
    return merge(leftArr,rightArr)

def merge(leftArr,rightArr):
    left_len = len(leftArr)
    right_len = len(rightArr)
    i,j = 0,0
    res = []
    while i < left_len and j < right_len:
        temp = abs(leftArr[i][0]-rightArr[j][0])
        
        if leftArr[i][0] >= rightArr[j][0]:
            if temp <= k:
                res.append(rightArr[j])
            j += 1
        else:
            if temp <= k:
                res.append(leftArr[i])
            i += 1
    return res + leftArr[i:] + rightArr[j:]

arr = countWiner(nums,k)
print(*sorted(arr))
        
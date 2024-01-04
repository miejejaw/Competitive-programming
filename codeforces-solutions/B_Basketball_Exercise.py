from heapq import heapify,heappop,heappush
from queue import deque
from collections import defaultdict
import math

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))
def STL(): return list(input())

def solve():
    n = I()
    arr1 = IL()
    arr2 = IL()
    
    nums1 = [0] + arr1
    nums2 = [0] + arr2
    
    for idx in range(2,n+1):
        nums1[idx] += max(nums2[idx-2],nums2[idx-1])
        nums2[idx] += max(nums1[idx-2],nums1[idx-1])
    
    print(max(nums1[-1],nums2[-1]))
        
T = 1
# T = I()
for _ in range(T):
    solve()
    # print(solve())
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
    n, m, k = IL()

    a = set()
    b = set()

    nums = IL()
    for num in nums:
        if num <= k:
            a.add(num)

    nums = IL()
    for num in nums:
        if num <= k:
            b.add(num)

    differenceA = list(a - b)
    differenceB = list(b - a)
    intersection = list(a & b)

    count = 0
    if len(differenceA) < k // 2:
        count += k // 2 - len(differenceA)

    if len(differenceB) < k // 2:
        count += k // 2 - len(differenceB)

    if count <= len(intersection):
        print("YES")
    else:
        print("NO")

# T = 1
T = I()
for _ in range(T):
    solve()
    # print(solve())
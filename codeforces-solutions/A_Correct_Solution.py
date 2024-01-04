from heapq import heapify,heappop,heappush
from queue import deque

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

num1 = list(ST())
num2 = ST()
num1.sort()

ind,n = 0,len(num1)
while ind < n and num1[ind] == "0":
    ind += 1
if ind < n:   
    num1[ind],num1[0] = num1[0],num1[ind]
num1 = "".join(num1)
if num1 == num2:
    print("OK")
else:
    print("WRONG_ANSWER")
    
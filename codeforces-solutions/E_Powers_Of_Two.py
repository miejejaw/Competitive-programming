from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n,k = IL()
res = []
p = 0
for bit in reversed(bin(n)):
    if bit == "1":
        res.append(2**p)
    p += 1
ind = 0
while ind < len(res) < k:
    if res[ind] > 1:
        temp = res[ind] // 2
        res[ind] = temp
        res.append(temp)
    else:
        ind += 1
if k == len(res):
    print("YES")
    print(*res)
else:
    print("NO")
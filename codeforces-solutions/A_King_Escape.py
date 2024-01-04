from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
ax,ay = IL()
bx,by = IL()
cx,cy = IL()

if (bx<ax and cx<ax) or (bx>ax and cx>ax):
    if (by<ay and cy<ay) or (by>ay and cy>ay):
        print("YES")
        exit()
print("NO")
from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

t = I()
for _ in range(t):
    n = I()
    word = list(ST())
    ind = 0
    for i in range(1,n):
        if word[i] <= word[ind]:
            ind = i
    ch = word.pop(ind)
    word.insert(0,ch)
    print("".join(word))
    
    
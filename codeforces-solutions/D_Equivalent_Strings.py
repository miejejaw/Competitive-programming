from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

def trav(word1,word2):
    
    if word1 == word2:
        return True
    
    n = len(word1)
    if n % 2 == 1:
        return False
    
    mid = n//2
    a = word1[:mid]
    aa = word1[mid:]
    b = word2[:mid]
    bb = word2[mid:]
    if trav(a,b) and trav(aa,bb):
        return True
    if trav(a,bb) and trav(aa,b):
        return True
    
    return False

ans = "NO"
if trav(ST(),ST()):
    ans = "YES"

print(ans)
from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))

n = I()
dic = defaultdict(list)
citys = set()
for _ in range(n):
    x,y = IL() 
    if x in dic:
        citys.add(x)
    if y in dic:
        citys.add(y)
    dic[x].append(y)
    dic[y].append(x)

ans = []   
for city in dic:
    if city not in citys:
        ind = city
        break
    
seen = set()
while ind not in seen:
    seen.add(ind)
    ans.append(ind)
    for i in dic[ind]:
        if i not in seen:
            ind = i
            break
print(*ans)
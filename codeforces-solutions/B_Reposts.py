from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))

n = I()
dic = defaultdict(list)
queue = []
for _ in range(n):
    name1,_,name2 = ST().split()
    dic[name2.lower()].append(name1.lower())
    if not queue:
        queue.append(name2.lower())

count = 0
visited = set()
while queue:
    temp = []
    for name2 in queue:
        if name2 not in visited:
            visited.add(name2)
            for name1 in dic[name2]:
                if name1 not in visited:
                    temp.append(name1) 
    count += 1
    queue = temp
    
print(count) 




    
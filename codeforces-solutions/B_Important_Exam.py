from collections import defaultdict
n,m = map(int,input().split())
grades = []
total = 0
for _ in range(n):
    grades.append(input())
points = list(map(int, input().split()))
for i in range(m):
    dic = defaultdict(int)
    for grade in grades:
        dic[grade[i]] += 1
        
    total += points[i]*max(dic.values())
print(total)
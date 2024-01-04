import collections
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
dic = collections.defaultdict(int)
for _ in range(m):
    name = input()
    dic[name] += 1

temp = sorted(dic.values())
a = 0
b = 0
size = len(temp)
for ind in range(size):
    a += temp[~ind]*arr[ind]
    b += temp[~ind]*arr[~ind]

print(a,b)
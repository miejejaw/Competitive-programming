import math
def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
nums = [1]*n
l = int(math.sqrt(n+1))

for i in range(2,l+1):
    if nums[i] == 1:
        for j in range(i*i,n+1,i):
            nums[j] = 2
            
if n >= 3:
    print(2)
else:
    print(1)
print(*nums)

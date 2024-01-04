def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

x = I()
nums = [1]

d = 2
while d*d <= x:
    num = 1
    while x%d == 0:
        x //= d
        num *= d
    d += 1
    if num > 1:
        nums.append(num)
    f
nums.append(x)
nums.sort()

n = len(nums)
_min = [float("inf"),float("inf")]
def back(res,ind):
    global _min,nums,n
    if ind < n:
        
        res[0] *= nums[ind]    
        back(res,ind+1)
        res[0] //= nums[ind]
        res[1] *= nums[ind]
        back(res,ind+1)
        res[1] //= nums[ind]
        
        return
    if max(res) < max(_min):
        _min = res[:]
        
back([1,1],0)        
print(*_min)
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    min_ = min(a,b)
    max_ = max(a,b)
    ans = 0
    if min_ != max_:
        left = 0
        right = max_//3
        while left < right:
            mid = left + (right-left)//2
            if max_ - (mid*3) <= min_ - mid:
                right = mid 
            else:
                left = mid + 1
                
        if left > min_:
            left = min_       
        ans = left        
        min_ = min(min_-left , max_-(left*3))
    print(ans + min_//2)
        
        
    
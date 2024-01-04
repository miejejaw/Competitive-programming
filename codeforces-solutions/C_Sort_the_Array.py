n = int(input())
arr = list(map(int,input().split()))
beg,end = -1,-1
ans = "yes"
for ind in range(1,n): 
    if arr[ind-1]>arr[ind]:
        if beg==-1:
            beg = ind-1
        end = ind
start,last= beg,end
while end>beg:
    arr[beg],arr[end] = arr[end],arr[beg]
    beg += 1
    end -= 1
for ind in range(1,n):
    if arr[ind]<arr[ind-1]:
        ans = "no"
        break   
print(ans)
if ans=="yes":
    if start==-1:
        start=last=0
    print(start+1,last+1)

    
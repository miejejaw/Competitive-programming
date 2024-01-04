n = int(input())
 
arr = list(map(int,input().split()))
arr.sort()
n1,n2,n3 = [arr[0]],[],[]
 
if arr[-1]==0:
    n2 = [arr[-2],arr[-3]]
    n3 = [arr[-1]]
    n -= 3
else:
    n2 = [arr[-1]]
    n -= 1
    
for i in range(1,n):
    n3.append(arr[i])
print(1,*n1)
print(len(n2),*n2)
print(len(n3),*n3)
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
result = []
for i in range(len(arr[0])):
    temp = set()
    for word in arr:
        temp.add(word[i])
    temp.discard('?')
    if len(temp)>1:
        result.append('?')
    elif len(temp)==0:
        result.append('x')
    else:
        result.append(temp.pop())
print("".join(result))
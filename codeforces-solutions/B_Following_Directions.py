t = int(input())
for _ in range(t):
    n = int(input())
    ways = input()
    path = [0,0]
    ans = "NO"
    for way in ways:
        if way=="U":
            path[0] += 1
        elif way=="D":
            path[0] -= 1
        elif way=="L":
            path[1] -= 1
        else:
            path[1] += 1
            
        if path == [1,1]:
            ans = "YES"
            break
    print(ans)
    

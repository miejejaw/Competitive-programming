from itertools import accumulate
from collections import defaultdict

def I(): return int(input())
def ST(): return input()
def IL(): return list(map(int, input().split()))
def ILS(): return sorted(map(int, input().split()))

n = I()
st = [[1,0]]
for _ in range(n):
    command = ST()
    if command == "add":
        st[-1][1] += 1
    elif command == "end":
        iteration,adds = st.pop()
        st[-1][1] += iteration*adds
    else:
        _,loop = command.split() 
        st.append([int(loop),0])

if st[-1][1] > 2**32 - 1:
    print("OVERFLOW!!!")       
else:
    print(st[-1][1])                                                    
     
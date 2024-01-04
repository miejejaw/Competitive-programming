import collections

word = input()
word = collections.Counter(word)
b,s,c = map(int,input().split())
pb,ps,pc = map(int,input().split())
r = int(input())
ans = 0
mc,ms,mb = word["C"],word["S"],word["B"]
while r > 0:
    if








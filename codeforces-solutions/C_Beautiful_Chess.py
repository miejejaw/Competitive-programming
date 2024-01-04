t = int(input())
for _ in range(t):
    row=col=0
    flag = False
    a = input()
    for i in range(8):
      arr = input()
      n = arr.count("#")
      if not flag and n==2:
          flag = True
      elif flag and n==1 and row==0:
          col = arr.index("#")+1
          row = i+1
    print(row,col)
import collections
word = input()
dic = collections.defaultdict(list)
n = len(word)
ans = n
for ind,ch in enumerate(word):
    if ch in dic:
        dic[ch][1] = max(dic[ch][1] , ind-dic[ch][0])
        dic[ch][0] = ind
    else:
        dic[ch].append(ind)
        dic[ch].append(ind+1)
for key,val in dic.items():
    ans = min(ans,max(val[1],n-val[0]))    
print(ans)

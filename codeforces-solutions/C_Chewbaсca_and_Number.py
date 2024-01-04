num = int(input())
result = 0
a = 1
while num:
    if 9==num:
       result += num*a
       break
    temp = num%10
    if temp>4:
        temp = 9-temp
    
    result += temp*a
    a *= 10
    num //= 10
    
        
print(result)
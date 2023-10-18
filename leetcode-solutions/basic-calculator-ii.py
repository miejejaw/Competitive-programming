import re

class Solution:
    def getNumbers(self, s):
        s = s.replace(" ","")
        pattern = r'[+|\-|*|/]'
        nums = re.split(pattern, s)
        return list(map(int,nums))

    def calculate(self, s: str) -> int:
        
        nums = self.getNumbers(s)
        op = [ char for char in s if char in "+-*/"]

        length = len(nums)
        st = [nums[0]]

        for idx in range(1,length):
            if op[idx-1] is "*":
                st[-1] *= nums[idx]
            elif op[idx-1] is "/":
                if st[-1] < 0:
                    st[-1] = ceil(st[-1]/nums[idx])
                else:
                    st[-1] //= nums[idx]
            elif op[idx-1] is "-":
                st.append(-nums[idx])
            elif op[idx-1] is "+":
                st.append(nums[idx])

        return sum(st)
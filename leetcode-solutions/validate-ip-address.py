class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if "." in queryIP:
            return self.isIPv4(queryIP.split("."))
        else:
            return self.isIPv6(queryIP.split(":"))

    def isIPv4(self, arr):
        if len(arr) != 4: return "Neither"
        for q in arr:
            if not q.isnumeric() or int(q)>255 or (q[0]=="0" and len(q)>1):
                return "Neither"
        
        return "IPv4"

    def isIPv6(self, arr):
        if len(arr) != 8: return "Neither"
        chars  = "1234567890ABCDEFabcdef"
        for q in arr:
            if not q or len(q) > 4: return "Neither"
            for char in q:
                if char not in chars: return "Neither"
        
        return "IPv6"

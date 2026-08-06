class Solution:
    def scoreOfString(self, s: str) -> int:
        ss=[]
        for i in range(len(s)-1):
            ss.append(abs(ord(s[i])-ord(s[i+1])))
        return sum(ss)
        
        
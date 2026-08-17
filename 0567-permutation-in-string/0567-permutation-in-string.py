class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        need, window={}, {}
        for c in s1:
            need[c]=need.get(c, 0)+1
        left=0
        for right,c in enumerate(s2):
            window[c]=window.get(c, 0)+1

            if right-left+1>len(s1):
                x=s2[left]
                window[x]-=1
                window.pop(x) if window[x]==0 else None
                left+=1
            if window==need:
                return True
        return False

            
        
        
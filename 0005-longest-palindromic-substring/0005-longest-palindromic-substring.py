class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        max_length=1
        def expand(left, right):
            while left>=0 and right< len(s) and s[left]==s[right]:
                left -=1
                right +=1
            return left+1, right -1
        for i in range(len(s)):
            left, right = expand(i,i)
            if right-left+1>max_length:
                start=left
                max_length=right-left+1
            left, right = expand(i, i+1)
            if right-left+1>max_length:
                start=left
                max_length=right-left+1
        return s[start:start + max_length]
        
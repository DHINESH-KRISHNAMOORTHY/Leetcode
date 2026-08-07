class Solution:
    def isPalindrome(self, x: int) -> bool:
        word=str(x)
        if word==word[::-1]:
            return True
        else:
            return False        
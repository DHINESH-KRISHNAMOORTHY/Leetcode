class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        a=list(set(str(n)))
        digit=[]
        for i in range(len(a)):
            digit.append(str(n).count(str(a[i]))*int(a[i]))
        return sum(digit)
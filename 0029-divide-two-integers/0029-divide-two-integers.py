class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INI_MAX = 2**31 - 1
        INI_MIN = -(2**31)

        if dividend == INI_MIN and divisor == -1:
            return INI_MAX
        negative=(dividend<0)^(divisor<0)
        dividend=abs(dividend)
        divisor = abs(divisor)
        quotient=0
        for i in range(31, -1, -1):
            if (divisor <<i) <= dividend:
                dividend -= divisor <<i
                quotient += 1<<i
        return -quotient if negative else quotient
        
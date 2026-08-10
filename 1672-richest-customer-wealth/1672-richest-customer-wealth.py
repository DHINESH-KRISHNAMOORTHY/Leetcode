class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for account in accounts:
            wealth = sum(account)
            if wealth>richest:
                richest=wealth
        return richest
        
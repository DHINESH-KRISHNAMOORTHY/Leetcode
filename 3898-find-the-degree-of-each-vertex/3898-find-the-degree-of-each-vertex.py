class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        m=[]
        for i in range(len(matrix)):
            m.append(sum(matrix[i]))
        return m
        



        
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        m=[]
        for i in range(len(matrix)):
            m.append(matrix[i].count(1))
        return m
        



        
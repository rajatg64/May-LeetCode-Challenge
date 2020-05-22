class Solution:
    # using Dynamic Programming
    def countSquares(self, matrix: List[List[int]]) -> int:        
        m=len(matrix)
        if not m:return 0
        n=len(matrix[0])
        count=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i>0 and j>0:
                        matrix[i][j]+=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                    count+=matrix[i][j]
        return count

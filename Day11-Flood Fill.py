class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.newColor = newColor
        self.oldColor = image[sr][sc]
        
        def dfs(sr, sc):
            if sr < 0 or sr >= len(self.image) or sc < 0 or sc >= len(self.image[sr]):
                return
            if self.image[sr][sc] != self.oldColor or self.image[sr][sc] == self.newColor:
                return
            self.image[sr][sc] = self.newColor
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(sr + dr, sc + dc)
            
        dfs(sr, sc)
        return self.image
class Solution:
    def slope(self, firstPoint, secondPoint):
        if (firstPoint[0] - secondPoint[0]) == 0:
            return 0
        slope = (firstPoint[1] - secondPoint[1]) / (firstPoint[0] - secondPoint[0])
        return slope
        
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        
        
        firstPoint = coordinates[0]
        secondPoint = coordinates[1]
        
        gslope = self.slope(firstPoint, secondPoint)
        
        for i in range(2, len(coordinates)):
            slope = self.slope(firstPoint, coordinates[i])
            if slope !=  gslope:
                return False
            
        return True
        
        
        
        
        
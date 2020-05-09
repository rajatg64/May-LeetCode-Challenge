class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binarySearch(num,low,high):
            if low > high:
                return False
            mid = low + (high-low)//2
            
            if mid**2 == num:
                return True
            
            if mid**2 > num:
                return binarySearch(num,low, mid-1)
            else:
                return binarySearch(num,mid+1, high)
        return binarySearch(num,1,num)
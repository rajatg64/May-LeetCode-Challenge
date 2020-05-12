class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def find(nums, l, h):
            if l > h:
                return None
            mid = l + (h-l)//2
            if l == h:
                return nums[h]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    return find(nums, mid+2, h)
                else:
                    return find(nums, l, mid)
            else:
                if nums[mid] == nums[mid-1]:
                    return find(nums, mid+1, h)
                else:
                    return find(nums, l, mid-1)
        return find(nums,0, len(nums)-1)
                    
            
            
        
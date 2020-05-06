class Solution:
    
    # Solution 1 using Moore's Voting Algorithm
    
    def findCandidate(self,nums):
        max_index = 0
        count = 1
    
        for i in range(1, len(nums)):
            if nums[max_index] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                max_index = i
                count = 1
        return nums[max_index]
    
    def majorityElement(self, nums: List[int]) -> int:
        candidate = self.findCandidate(nums)
        c = nums.count(candidate)
        if c > len(nums)//2:
            return candidate
        return -1
    
    # Solution 2 using hashtables
    '''
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                hashtable[nums[i]] += 1
            else:
                hashtable[nums[i]] = 1
                
        for key in hashtable:
            
            if hashtable[key] > len(nums)//2:
                return key
       '''         
        
                
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i in nums:
                i+=1
            else:
                return i
        return -1
            
        
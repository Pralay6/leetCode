class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp ={}
        for i in nums:
            if i in temp and temp[i]>=1:
                return True
            temp[i] = temp.get(i,0) + 1
        return False
    
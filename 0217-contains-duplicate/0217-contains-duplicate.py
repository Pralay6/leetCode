class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using hashset
        #space = O(n)
        #time = O(n)
        hashset = set()
        
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
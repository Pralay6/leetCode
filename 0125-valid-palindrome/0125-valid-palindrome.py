class Solution:
    def isPalindrome(self, s: str) -> bool:
        res_str = ''
        
        for i in s:
            if i.isalnum():
                res_str+=i.lower()
        return res_str == res_str[::-1]
                
            
        
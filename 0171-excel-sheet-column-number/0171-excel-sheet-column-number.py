class Solution(object):
    def titleToNumber(self, s):
        result = 0
        for i in s:
            d = ord(i)-ord('A')+1
            result = result * 26 + d
        return result 
        
class Solution(object):
    def plusOne(self, digits):
        idx = len(digits)-1
        while idx >= 0:
            if(digits[idx] == 9):
                digits[idx] = 0
            else:
                digits[idx] +=1
                return digits
            idx-=1
        
        return [1] + digits
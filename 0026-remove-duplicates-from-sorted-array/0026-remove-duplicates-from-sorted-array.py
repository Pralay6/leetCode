class Solution(object):
    def removeDuplicates(self, n):
        l = 1
        for r in range(1 , len(n)):
            if n[r] != n[r-1]:
                n[l] = n[r]
                l+=1
        return l
                
            
                
                                                                                                                                                                                                                              
        
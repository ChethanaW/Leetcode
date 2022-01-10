class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dictionary = {}
        
        for e in nums:
            if e in dictionary.keys(): 
                return e
                
            else:
                dictionary[e] = 1
            
            
    
        
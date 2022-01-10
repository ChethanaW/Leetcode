class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
#         timed out bcs worst case run time is o(n^2)
#         count = 0
#         for e in nums:
#             if e in nums[count+1:]:
#                 return e
            
#             count = count + 1
        
        dictionary = {}
        
        for e in nums:
            if e in dictionary.keys(): 
                return e
                
            else:
                dictionary[e] = 1
            
            
    
        
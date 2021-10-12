class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        newA = list(set(nums))
        
        for i in range(0, len(newA)):
            
            if newA[0] != 0:
                return 0
            elif i == len(newA) -1: #at the end
                return newA[i] +1
            elif newA[i] - newA[i+1] != -1:
                return newA[i] +1
            else:
                continue
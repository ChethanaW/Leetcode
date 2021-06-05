class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        lo = 0
        hi = len(nums)-1
        
        while ( lo <= hi):
            index = (lo + hi)//2
            if (target <  nums[index]):
                hi =  index - 1
            elif (target >  nums[index]):
                lo =  index + 1
            else:
                return index
            
        return int(-1)
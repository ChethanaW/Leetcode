class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    result.append(i)
                    result.append(j)
                    return result
        

                    #  better solution from solutions
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         h = {} # map
#         for i, num in enumerate(nums):
#             n = target - num

#             if n not in h:
#                 h[num] = i
#             else:
#                 return [h[n], i]

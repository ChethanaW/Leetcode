class Solution:
    def reverseStr(self, s: str, k: int) -> str:
    # inspired from example solution
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return "".join(a)
    
    # my code breaks at once cases, passes all given and basic cases
#         new = ""
#         length_s = len(s)
#         count = 0
#         start_k = k
        
#         if k > length_s:
#             return s[::-1]
        
#         if k ==1:
#             return s
        
#         for l in s:
#             count += 1
            
#             if count == k or (count == length_s and count < k ):
#                 reverse = s[k-start_k:k][::-1]
#                 new = new[:-start_k+1]
#                 new += reverse
#                 k = k + 2*k
#             else:
#                 new += l
                
#         return new
        
            
        
            
            
            
            
            
            
# abc , k =2 -> cba

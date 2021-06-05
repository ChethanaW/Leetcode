class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            import math
            
            
            sum = 0
            
            if len(piles) == h:
                return max(piles)
            else:
                mi = 1
                ma = max(piles)
                
                while mi < ma:
                    pivot = ( mi + ma )//2
                    
                    for p in piles:
                        sum = sum + math.ceil (p/pivot)
                        
                    if (sum <= h):
                        ma = pivot 
                    else:
                        mi = pivot + 1
                        
                    sum = 0
                    
                return mi
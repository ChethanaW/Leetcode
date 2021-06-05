class Solution:
    def toLowerCase(self, s: str) -> str:
        new  = ""
        
        for e in s:
            new += (e.lower())
            
        return new
            
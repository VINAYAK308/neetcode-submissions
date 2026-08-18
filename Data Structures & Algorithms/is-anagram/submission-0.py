from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = s.replace(" ", "").lower()
        s2 = t.replace(" ", "").lower()

        if len(s1) != len(s2):
            return False
        
        return sorted(s1) == sorted(s2)
        

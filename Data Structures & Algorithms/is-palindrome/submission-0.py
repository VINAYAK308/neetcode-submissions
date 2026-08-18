class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = s.replace(" ", "")
        result = ''.join(ch.lower() for ch in s if ch.isalnum())
        start = 0
        end = len(result) - 1
        
        while start < end:
            if result[start] != result[end]:
                return False
            start+= 1
            end -= 1
        return True
        
        
class Solution:

    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        
        for idx in range(0, len(s)):

            while not s[front].isalnum():       
                front += 1
                if not front < len(s):
                    return True
            while not s[back].isalnum():
                back -= 1
                if not back >= 0:
                    return True

            if front >= back:
                return True

            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
            
        return False
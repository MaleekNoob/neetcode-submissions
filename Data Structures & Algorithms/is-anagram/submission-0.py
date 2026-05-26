from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        for ch in t:
            if not (s_dict[ch] - 1) >= 0:
                return False
            s_dict[ch] -= 1

        return True
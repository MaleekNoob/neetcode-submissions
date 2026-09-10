class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need_count = {}

        for char in t:
            need_count[char] = need_count.get(char, 0) + 1

        window_count = {}

        left = 0
        have = 0
        need = len(need_count)

        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # This requirement has just become satisfied
            if char in need_count and window_count[char] == need_count[char]:
                have += 1

            # Window is valid, so try shrinking it
            while have == need:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right + 1]

                left_char = s[left]
                window_count[left_char] -= 1

                # Removing this character broke a requirement
                if left_char in need_count and window_count[left_char] < need_count[left_char]:
                    have -= 1

                left += 1

        return result
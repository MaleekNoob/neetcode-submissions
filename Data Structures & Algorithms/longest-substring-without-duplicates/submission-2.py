class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0

        unique_chars = set()

        for right in range(0, len(s)):
            while s[right] in unique_chars:
                # shrink window such that it drops all chars till that duplicate value
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len
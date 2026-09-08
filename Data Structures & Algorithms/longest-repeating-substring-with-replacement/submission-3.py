class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        max_window = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            max_freq  = max(frequency[s[right]], max_freq)

            window_len = right - left + 1
            replacements = window_len - max_freq

            while replacements > k:
                frequency[s[left]] -= 1
                left += 1

                window_len = right - left + 1
                replacements = window_len - max_freq

            max_window = max(window_len, max_window)

        return max_window
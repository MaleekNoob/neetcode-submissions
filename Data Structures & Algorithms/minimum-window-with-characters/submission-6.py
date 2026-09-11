class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_count = {}
        for char in t:
            need_count[char] = need_count.get(char, 0) + 1

        have_count = {}

        min_len = float('inf')
        have = 0
        left = 0
        need = len(need_count)
        result = ""

        for right in range(len(s)):
            have_count[s[right]] = have_count.get(s[right], 0) + 1

            if s[right] in need_count and have_count[s[right]] == need_count[s[right]]:
                have += 1

            while need == have:
                wind_len = right - left + 1
                if wind_len < min_len:
                    min_len = wind_len
                    result = s[left: right + 1]

                have_count[s[left]] -= 1

                if s[left] in need_count and have_count[s[left]] < need_count[s[left]]:
                    have -= 1

                left += 1

        return result
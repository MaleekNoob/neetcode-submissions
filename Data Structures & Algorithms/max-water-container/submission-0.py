class Solution:
    def maxArea(self, heights: List[int]) -> int:
        back = 0
        front = len(heights) - 1

        max_vol = 0

        while back < front:
            max_vol = max(min(heights[back], heights[front]) * (front - back), max_vol)

            if heights[back] > heights[front]:
                front -= 1
            else:
                back += 1

        return max_vol

        
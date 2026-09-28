class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx in range(len(heights)):

            while stack and heights[stack[-1]] > heights[idx]:
                height_idx = stack.pop()
                height = heights[height_idx]

                left_boundary = stack[-1] if stack else -1
                width = idx - left_boundary - 1

                area = height * width
                max_area = max(max_area, area)

            stack.append(idx)

        while stack:
            height_idx = stack.pop()
            height = heights[height_idx]

            left_boundary = stack[-1] if stack else -1
            width = len(heights) - left_boundary - 1

            area = height * width
            max_area = max(max_area, area)

        return max_area
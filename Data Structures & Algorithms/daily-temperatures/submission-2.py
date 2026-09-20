class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for temp_idx in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[temp_idx]:
                prev = stack.pop()
                result[prev] = temp_idx - prev

            stack.append(temp_idx)

        return result
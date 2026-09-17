class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of temperatures
        
        for i, temp in enumerate(temperatures):
            # Pop elements from stack while the current temperature is warmer
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            # Push the current day's index onto the stack
            stack.append(i)
            
        return result
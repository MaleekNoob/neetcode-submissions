from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        idx_dq = deque()
        win_size = 0
        result = []

        for right in range(len(nums)):
            win_size = right - left + 1

            while idx_dq and idx_dq[0] < left:
                idx_dq.popleft()

            while idx_dq and nums[idx_dq[-1]] <= nums[right]:
                idx_dq.pop()
            
            idx_dq.append(right)

            if win_size == k:
                result.append(nums[idx_dq[0]])
                left += 1 

        return result
        
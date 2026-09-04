from collections import Counter

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for idx, val in enumerate(nums):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            back = idx + 1
            front = len(nums) - 1

            while back < front:
                total = nums[idx] + nums[front] + nums[back]

                if total == 0:
                    result.append([nums[idx], nums[front], nums[back]])

                    back += 1
                    front -= 1

                    while back < front and nums[back] == nums[back - 1]:
                        back += 1
                    while back < front and nums[front] == nums[front + 1]:
                        front -= 1

                elif total < 0:
                    back += 1
                else:
                    front -= 1

        return result
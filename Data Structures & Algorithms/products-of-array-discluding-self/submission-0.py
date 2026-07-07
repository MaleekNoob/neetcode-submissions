class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i, num in enumerate(nums):
        #     prod = 1
        #     for j, num_z in enumerate(nums):
        #         if j != i:
        #             prod *= num_z
        #     output.append(prod)
        
        # return output

        output = []
        left_to_right = []
        right_to_left = []
        prod = 1
        for num in nums:
            prod = prod * num
            left_to_right.append(prod)
        prod = 1
        for num in range(len(nums) - 1, -1, -1):
            prod = prod * nums[num]
            right_to_left.append(prod)
        right_to_left.reverse()
        res = []

        if (len(right_to_left) != len(left_to_right)) or (len(nums) != len(right_to_left)):
            exit(1)
                
        for i, num in enumerate(nums):
            a = 1
            b = 1
            if (i - 1) >= 0:
                a = left_to_right[i - 1]
            if (i + 1) < len(nums):
                b = right_to_left[i + 1]
                
            val = a * b
            res.append(val)
            
        return res
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        right_max = 0
        left_max = 0

        water = 0

        while left < right:
            '''
            We will never encounter situation where we are processing left side without right 
            being absolute max
            OR
            processing right without left being absolute max

            This structure would allow us to process left using relative left maximum
            (which would be lesser than right absolute maxima) at any given point
            '''

            if height[left] < height[right]:
                # case: if right is higher and left side is limiting factor

                if height[left] >= left_max:
                    # as right would always be higher here
                    # check if left (the limiting factor) is sufficient to hold water
                    # or whether its another higher left/limiting wall
                    left_max = height[left]

                else:
                    # if left is limiting factor and is bigger than current wall
                    # count water
                    water += left_max - height[left]

                left += 1
            
            else:
                # right side is limiting wall and left is always greater here

                if height[right] >= right_max:
                    # if its another bigger right limit/wall
                    right_max = height[right]
                else:
                    # if not then its water
                    # because left is absolute maximum for now, and right is relative max
                    # therefore we can count water based on relative max (right)
                    water += right_max - height[right]

                right -= 1

        return water
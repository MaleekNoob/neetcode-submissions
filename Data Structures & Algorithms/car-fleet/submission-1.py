class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        pos_stack = []
        for pos, spd in cars:
            distance = (target - pos) / spd
            if not pos_stack or distance > pos_stack[-1]:
                pos_stack.append(distance)
        return len(pos_stack)
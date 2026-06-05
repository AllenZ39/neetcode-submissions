class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = dict(zip(position, speed))
        sorted_dict = dict(sorted(m.items(), reverse=True))
        stack = []
        for position in sorted_dict:
            time = (target - position) / sorted_dict[position]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for n in range(len(position)):
            cars.append((position[n], speed[n]))
        cars.sort(reverse=True)
        stack = []
        for pos, spd in cars:
            if not stack:
                stack.append((pos, spd))
            else:
                newtime = (target - pos)/spd
                top = stack[-1]
                toptime = (target - top[0])/top[1]
                if newtime > toptime:
                    stack.append((pos, spd))
        return len(stack)
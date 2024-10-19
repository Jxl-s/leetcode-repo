class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for weight in asteroids:
            if weight > 0:
                stack.append(weight)
            else:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(weight)
                else:
                    destroyed = False
                    while len(stack) > 0 and stack[-1] > 0 and -weight >= stack[-1]:
                        if -weight <= stack.pop():
                            destroyed = True
                            break
                    
                    if not destroyed:
                        if len(stack) > 0 and stack[-1] < 0:
                            stack.append(weight)
                        elif len(stack) == 0:
                            stack.append(weight)

        return stack
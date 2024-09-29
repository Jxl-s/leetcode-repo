from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state = []
        for weight in asteroids:
            while state and weight < 0 and state[-1] > 0:
                prev = state.pop()
                if prev > -weight:
                    state.append(prev)
                    break
                elif prev == -weight:
                    break
            else:
                state.append(weight)

        return state

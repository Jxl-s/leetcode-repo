class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        flattened = [x for row in board for x in row]

        target = [1, 2, 3, 4, 5, 0]
        neighbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        visited = set()
        queue = deque()
        queue.append((flattened, flattened.index(0), 0)) # board, zero, moves

        while len(queue) > 0:
            current, zero, moves = queue.popleft()
            if current == target:
                return moves
            
            tuple_key = tuple(current)
            if tuple_key in visited:
                continue
            
            visited.add(tuple_key)
            for neighbor in neighbors[zero]:
                copy = current[:]
                copy[zero], copy[neighbor] = copy[neighbor], copy[zero]
                if copy == target:
                    return moves + 1

                queue.append((copy, neighbor, moves + 1))
        
        return -1
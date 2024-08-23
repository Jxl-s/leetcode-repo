class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        for i in range(len(mat)):
            total = 0
            for j in range(len(mat[i])):
                total += mat[i][j]
            
            if total > 1:
                for j in range(len(mat[i])):
                    if mat[i][j] == 1:
                        mat[i][j] = 2
        
        for j in range(len(mat[0])):
            total = 0
            for i in range(len(mat)):
                total += mat[i][j]
            
            if total > 1:
                for i in range(len(mat)):
                    if mat[i][j] == 1:
                        mat[i][j] = 2
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1

        return count
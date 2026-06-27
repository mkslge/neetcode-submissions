class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        states = [[-1 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

        def dp(i, j):
            if i + j == len(s3):
                return True
            elif states[i][j] == -1:
                i1 = i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j)
                i2 = j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1)
                states[i][j] = 1 if i1 or i2 else 0
                
            return states[i][j] == 1
        return dp(0,0)
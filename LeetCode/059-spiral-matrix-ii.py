class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for i in range(n)]
        i, l, u, r, d = 1, 0, 0, n-1, n-1
        while (i <= n*n):
            for j in range(l, r+1):
                res[u][j] = i
                i += 1
            u+=1
            for j in range(u, d+1):
                res[j][r] = i
                i += 1
            r-=1
            for j in range(r, l-1, -1):
                res[d][j] = i
                i +=1
            d-=1
            for j in range(d, u-1, -1):
                res[j][l] = i
                i+=1
            l+=1
        return res

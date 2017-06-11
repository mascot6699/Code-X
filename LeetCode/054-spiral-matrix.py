class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a = []
        if not matrix:
            return a
        m, n = len(matrix), len(matrix[0])
        l , r, u , d = 0 , n-1, 0, m-1
        while l < r and u < d:
            a.extend([matrix[l][i] for i in range(l,r)])
            a.extend([matrix[i][r] for i in range(u,d)])
            a.extend([matrix[d][i] for i in range(r,l, -1)])
            a.extend([matrix[i][l] for i in range(d,u,-1)])
            l , r, u , d = l+1 , r-1, u+1 , d-1
        if l == r:
            a.extend([ matrix[i][l] for i in range(u, d+1)])
        elif u == d:
            a.extend([ matrix[u][i] for i in range(l,r+1)])
        return a

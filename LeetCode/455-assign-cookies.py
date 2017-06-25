class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        content_count = 0
        g = sorted(g)
        s = sorted(s)
        j = 0
        len_g = len(g)
        for i, quantity in enumerate(s):
            if j == len_g:
                break
            if quantity >= g[j]:
                content_count += 1
                j += 1
        return content_count

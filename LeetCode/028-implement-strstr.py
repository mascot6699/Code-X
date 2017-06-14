
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_needle > len_haystack:
            return -1

        BASE = 26
        needle_hash = functools.reduce(lambda h, c: h * BASE + ord(c), needle, 0)
        haystack_hash = functools.reduce(lambda h, c: h * BASE + ord(c), haystack[:len_needle], 0)
        power_of_last = BASE ** (len_needle - 1)

        for i in range(len_needle, len_haystack):
            print(haystack[i-len_needle:i])
            if (needle_hash == haystack_hash and needle == haystack[i-len_needle:i]):
                return i - len_needle

            haystack_hash -= ord(haystack[i - len_needle]) * power_of_last
            haystack_hash = (BASE * haystack_hash) + ord(haystack[i])

        if (needle_hash == haystack_hash and needle == haystack[-len_needle:]):
            return len_haystack-len_needle

        return -1

print(Solution.strStr("A", "mississipi", "issi"))


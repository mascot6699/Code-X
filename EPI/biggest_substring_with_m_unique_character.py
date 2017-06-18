MAX_CHARS = 26
def isValid(count, k):
    val = 0
    for i in xrange(MAX_CHARS):
        if count[i] > 0:
            val += 1
    return (k >= val)
 
def mUniques(s, k):
    u, n = 0, len(s)
    count = [0] * MAX_CHARS
    for i in xrange(n):
        if count[ord(s[i])-ord('a')] == 0:
            u += 1
        count[ord(s[i])-ord('a')] += 1
    if u < k:
        print "Not enough unique characters"
        return
    curr_start, curr_end, max_window_size, max_window_start = 0 , 0, 1, 0
    count = [0] * len(count)
    count[ord(s[0])-ord('a')] += 1

    for i in xrange(1,n):
        count[ord(s[i])-ord('a')] += 1
        curr_end+=1

        while not isValid(count, k):
            count[ord(s[curr_start])-ord('a')] -= 1
            curr_start += 1
        if curr_end-curr_start+1 > max_window_size:
            max_window_size = curr_end-curr_start+1
            max_window_start = curr_start
 
    print "Max substring is : " + s[max_window_start:] + " with length " + str(max_window_size)
 
s = "aabacbebebe"
k = 3
mUniques(s, k)
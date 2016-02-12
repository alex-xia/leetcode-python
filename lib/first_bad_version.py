__author__ = 'axia'

'''
 You are a product manager and currently leading a team to develop a new product. Unfortunately,
 the latest version of your product fails the quality check. Since each version is developed based on the previous version,
 all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def bs(beg, end):
            if beg == end:
                return beg
            mid = (beg + end) / 2
            if isBadVersion(mid):
                if mid == beg or not isBadVersion((mid-1)):
                    return mid
                else:
                    return bs(beg, mid-1)
            else:
                return bs(mid+1, end)
        return bs(1, n)
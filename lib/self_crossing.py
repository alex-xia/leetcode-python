__author__ = 'axia'
'''
 You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

Given x = [2, 1, 1, 2],


Return true (self crossing)

Example 2:

Given x = [1, 2, 3, 4],


Return false (not self crossing)

Example 3:

Given x = [1, 1, 1, 1],


Return true (self crossing)
'''

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) < 4:
            return False
        x.insert(0, 0)
        def check_type1(i):
            if i == len(x):
                return False
            if x[i] >= (x[i-2]-x[i-4]) and x[i-1] <= x[i-3]:
                return True
            elif x[i] == x[i-2] - x[i-4]:
                if i == len(x)-1:
                    return False
                return x[i+1] >= x[i-1] - x[i-3]
            elif x[i] > x[i-2]:
                return check_type1(i+1)
            else:
                if i == len(x)-1:
                    return False
                if x[i+1] >= x[i-1] - x[i-3] and x[i] >= x[i-2] - x[i-4]:
                    return True
                return check_type2(i+2)
        def check_type2(i):
            if i == len(x):
                return False
            if x[i] >= x[i-2]:
                return True
            return check_type2(i+1)

        return check_type1(4)


if __name__ == '__main__':
    s = Solution()
    # print s.isSelfCrossing([2,1,1,2])
    # print s.isSelfCrossing([1,2,3,4])
    # print s.isSelfCrossing([1,1,1,1])
    # print s.isSelfCrossing([1,1,2,1,1])
    print s.isSelfCrossing([3,3,4,2,2])
    # print s.isSelfCrossing([1,1,2,2,1,1])
    print s.isSelfCrossing([2,1,4,4,3,3,2,1,1])


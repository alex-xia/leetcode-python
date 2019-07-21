'''
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
'''

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        stack, next_stack = [0], []
        row = 1
        while len(stack) > 0:
            print row, stack
            position = stack.pop()
            if position == target:
                break
            next_stack.append(position-row)
            next_stack.append(position+row)
            # print stack, next_stack
            if len(stack) == 0:
                row += 1
                stack = next_stack
                next_stack = []
        return row-1


if __name__ == '__main__':
    sol = Solution()
    print sol.reachNumber(-1000000000)
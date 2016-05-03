__author__ = 'Qing'

'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def get_lefts(heights):
            print('>>>>>>', heights)
            lefts = []
            for i, h in enumerate(heights):
                if i == 0:
                    lefts.append(0)
                    continue
                if h == heights[i-1]:
                    lefts.append(lefts[i-1])
                elif h < heights[i-1]:
                    j = lefts[i-1]
                    while j >= 0 and heights[j] >= h:
                        j -= 1
                    lefts.append(j+1)
                else:
                    lefts.append(i)
            print('<<<<<<<', lefts)
            return lefts

        lefts = get_lefts(heights)
        rights = [len(heights) - i - 1 for i in get_lefts(heights[-1::-1])[-1::-1]]
        print(lefts)
        print(rights)
        res = 0
        for h, l, r in zip(heights, lefts, rights):
            res = max(res, h*(r-l+1))
        return res

if __name__ == '__main__':
    s = Solution()
    # print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([0,1,0,2,1,0,1,3,2,1,2,1]))

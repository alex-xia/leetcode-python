__author__ = 'axia'

'''
 Given two arrays of length m and n with digits 0-9 representing two numbers.
 Create the maximum number of length k <= m + n from digits of the two.
 The relative order of the digits from the same array must be preserved.
 Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:

nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''
import copy
import time

class Solution(object):
    def maxNumber(self, nums1, nums2, k): #[1,6,5,4,7,3,9,5,3,7,8,4,1,1,4],
                                            #[4,3,1,3,5,9],
                                            #21
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n1, n2 = len(nums1), len(nums2)
        ngn_lookup1 = self.get_ngn_lookup(nums1)
        ngn_lookup2 = self.get_ngn_lookup(nums2)

        def search(lookup, beg, n, min_digit):
            if beg >= n:
                return -1
            for d in range(9, -1, -1):
                p = lookup[beg][d]
                if p >= beg and n - p >= min_digit:
                    return p
            return -1

        self.res = []
        self.fronts = [(0,0)]
        def check(kk):
            print 'fronts=', self.fronts, 'kk=',kk
            if kk == k:
                return
            new_fronts = None
            memo = {}
            for front in self.fronts:
                i, j = front
                m1 = search(ngn_lookup1, i, n1, (k-kk)-(n2-j))
                if m1 >= i:
                    if m1+1 not in memo or j not in memo[m1+1]:
                        if not new_fronts or new_fronts[0] < nums1[m1]:
                            new_fronts = [nums1[m1], [(m1+1, j)]]
                        elif new_fronts[0] == nums1[m1]:
                            new_fronts[1].append((m1+1, j))
                        if m1+1 not in memo:
                            memo[m1+1] = set()
                        memo[m1+1].add(j)
                m2 = search(ngn_lookup2, j, n2, (k-kk)-(n1-i))
                if m2 >= j:
                    if i not in memo or m2+1 not in memo[i]:
                        if not new_fronts or new_fronts[0] < nums2[m2]:
                            new_fronts = [nums2[m2], [(i, m2+1)]]
                        elif new_fronts[0] == nums2[m2]:
                            new_fronts[1].append((i, m2+1))
                        if i not in memo:
                            memo[i] = set()
                        memo[i].add(m2+1)
            self.res.append(new_fronts[0])
            print self.res
            self.fronts = new_fronts[1]
            check(kk+1)

        check(0)
        return self.res


    @staticmethod
    # get next greatest number look up
    def get_ngn_lookup(nums):
        ngn_lookup = [[-1] * 10 for _ in range(len(nums))]
        p = [-1] * 10
        for i in range(len(nums)-1, -1, -1):
            p[nums[i]] = i
            ngn_lookup[i] = copy.copy(p)
        return ngn_lookup


    def maxNumber3(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        assert len(nums1) + len(nums2) >= k
        self.res = [[0,k]]
        code1, code2 = [self.recode(x) for x in [nums1, nums2]]
        if len(nums1) + len(nums2) == k:
            self.mix_max2(code1, code2)
            return self.expand(self.res)
        if len(nums1) > len(nums2):
            temp = copy.copy(nums1)
            nums1 = copy.copy(nums2)
            nums2 = temp
        self.memo = {}
        for i in range(0, min(k, len(nums1))+1):
            if i <= len(nums1) and k-i <= len(nums2):
                max1 = self.sub_max(copy.copy(nums1), i)
                max2 = self.sub_max(copy.copy(nums2), (k-i))
                h1, h2 = [self.hash(x) for x in [max1, max2]]
                if not h1 in self.memo or not h2 in self.memo[h1]:
                    self.mix_max(self.recode(max1), self.recode(max2))
                    if not h1 in self.memo:
                        self.memo[h1] = {}
                    self.memo[h1][h2] = True
                print max1, max2, self.res
        return self.expand(self.res)

    def hash(self, nums):
        h = ''
        for num in nums:
            h += str(num) + '#'
        return h[:-1]

    def recode(self, nums):
        res = [[nums[0], 1]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res[-1][1] += 1
            else:
                res.append([nums[i], 1])
        return res

    def sub_max(self, nums, k): #[3,4,6,5], [9,1,2,5,8,3], 5
        if k == 0:
            return []

        def dfs(arr, beg): #[8,6,9],[1,7,5],3
            if len(arr) == k:
                return arr
            i = len(arr)-1
            for i in range(beg, len(arr)):
                if i+1 < len(arr) and arr[i] < arr[i+1]:
                    break
            arr.pop(i)
            return dfs(arr, max(0,i-1))
        return dfs(nums, 0)

    def expand(self, code, i=0, j=None):
        j = len(code) if not j else j
        res = []
        for val, freq in code[i:j]:
            res.extend([val] * freq)
        return res

    def mix_max2(self, code1, code2): #[[1,2],[2,1]],[[1,2], [3,1]]
        def dfs(i, j, res_so_far):
            if i == len(code1) and j == len(code2):
                self.res = res_so_far
                return
            if i == len(code1):
                res_so_far.extend(code2[j:])
                self.res = self.greater2(self.res, res_so_far)
                return
            if j == len(code2):
                res_so_far.extend(code1[i:])
                self.res = self.greater2(self.res, res_so_far)
                return
            if code1[i][0] == code2[j][0]:
                if i+1 == len(code1) and j+1 == len(code2):
                    res_so_far.append([code1[i][0], code1[i][1]+code2[j][1]])
                    self.res = self.greater2(self.res, res_so_far)
                    return
                if i+1 == len(code1) or code1[i][1] > code2[j][1]:
                    res_so_far.append(code2[j])
                    dfs(i, j+1, res_so_far)
                    return
                if j+1 == len(code2) or code1[i][1] < code2[j][1]:
                    res_so_far.append(code1[i])
                    dfs(i+1, j, res_so_far)
                    return
                if code1[i+1][0] == code2[j+1][0]:
                    res_so_far.append(code1[i])
                    dfs(i+1, j, res_so_far)
                    return
                elif code1[i+1][0] < code2[j+1][0]:
                    res_so_far.append(code2[j])
                    dfs(i, j+1, res_so_far)
                    return
                else:
                    res_so_far.append(code1[i])
                    dfs(i+1, j, res_so_far)
                    return
            elif code1[i][0] < code2[j][0]:
                res_so_far.append(code2[j])
                dfs(i, j+1, res_so_far)
                return
            else:
                res_so_far.append(code1[i])
                dfs(i+1, j, res_so_far)
                return
        dfs(0, 0, [])

    def greater2(self, code1, code2):
        i, j = 0, 0
        offset1, offset2 = 0, 0
        while i < len(code1) and j < len(code2):
            if code1[i][0] == code2[j][0]:
                n1 = code1[i][1] - offset1
                n2 = code2[j][1] - offset2
                if n1 == n2:
                    i += 1
                    j += 1
                    offset1 = 0
                    offset2 = 0
                elif n1 < n2:
                    i += 1
                    offset1 = 0
                    offset2 += n2 - n1
                else:
                    j += 1
                    offset2 = 0
                    offset1 += n1 - n2
            elif code1[i][0] < code2[j][0]:
                return code2
            else:
                return code1
        return code1

    def mix_max(self, nums1, nums2):
        if len(nums1) == 0:
            self.res = self.greater(self.res, nums2)
            return
        if len(nums2) == 0:
            self.res = self.greater(self.res, nums1)
            return
        memo = {}
        def skip_equal(i, j, res_so_far):
            width = 0
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                res_so_far.append(nums1[i])
                i += 1
                j += 1
                width += 1
            return width, res_so_far

        def has_hope(res_so_far, next, res):
            i = 0
            while i < len(res_so_far):
                if res_so_far[i] < res[i]:
                    return False
                i += 1
            return True

        def dfs(i, j, res_so_far):
            print len(nums1), i, len(nums2), j, len(res_so_far)
            if not i in memo or not j in memo[i]:
                p = len(res_so_far)
                if i == len(nums1) and j == len(nums2):
                    self.res = res_so_far
                    return
                if i == len(nums1):
                    res_so_far.extend(nums2[j:])
                    self.res = self.greater(self.res, res_so_far)
                    return
                if j == len(nums2):
                    res_so_far.extend(nums1[i:])
                    self.res = self.greater(self.res, res_so_far)
                    return
                if nums1[i] == nums2[j]:
                    if has_hope(res_so_far, nums1[i], self.res):
                        width, res_so_far = skip_equal(i, j, res_so_far)
                        dfs(i, j+width, copy.copy(res_so_far))
                        dfs(i+width, j, copy.copy(res_so_far))
                    return
                if nums1[i] > nums2[j]:
                    if has_hope(res_so_far, nums1[i], self.res):
                        res_so_far.append(nums1[i])
                        dfs(i+1, j, res_so_far)
                    return
                else:
                    if has_hope(res_so_far, nums2[j], self.res):
                        res_so_far.append(nums2[j])
                        dfs(i, j+1, res_so_far)
                if i not in memo:
                    memo[i] = {}
                memo[i][j] = True
            return memo[i][j]
        dfs(0, 0, [])

    def greater(self, nums1, nums2):
        for i in xrange(len(nums1)):
            if nums1[i] > nums2[i]:
                return nums1
            if nums1[i] < nums2[i]:
                return nums2
        return nums1


if __name__ == '__main__':
    sol = Solution()
    # print sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
    # print sol.maxNumber([6,7], [6,0,4], 5)
    # print sol.maxNumber([3,9],[8,9],3)
    # nums1 =[4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2]
    # nums2 = [9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
    # print sol.maxNumber(nums1, nums2, 60)

    # nums1 = [8,9,7,3,5,9,1,0,8,5,3,0,9,2,7,4,8,9,8,1,0,2,0,2,7,2,3,5,4,7,4,1,4,0,1,4,2,1,3,1,5,3,9,3,9,0,1,7,0,6,1,8,5,6,6,5,0,4,7,2,9,2,2,7,6,2,9,2,3,5,7,4,7,0,1,8,3,6,6,3,0,8,5,3,0,3,7,3,0,9,8,5,1,9,5,0,7,9,6,8,5,1,9,6,5,8,2,3,7,1,0,1,4,3,4,4,2,4,0,8,4,6,5,5,7,6,9,0,8,4,6,1,6,7,2,0,1,1,8,2,6,4,0,5,5,2,6,1,6,4,7,1,7,2,2,9,8,9,1,0,5,5,9,7,7,8,8,3,3,8,9,3,7,5,3,6,1,0,1,0,9,3,7,8,4,0,3,5,8,1,0,5,7,2,8,4,9,5,6,8,1,1,8,7,3,2,3,4,8,7,9,9,7,8,5,2,2,7,1,9,1,5,5,1,3,5,9,0,5,2,9,4,2,8,7,3,9,4,7,4,8,7,5,0,9,9,7,9,3,8,0,9,5,3,0,0,3,0,4,9,0,9,1,6,0,2,0,5,2,2,6,0,0,9,6,3,4,1,2,0,8,3,6,6,9,0,2,1,6,9,2,4,9,0,8,3,9,0,5,4,5,4,6,1,2,5,2,2,1,7,3,8,1,1,6,8,8,1,8,5,6,1,3,0,1,3,5,6,5,0,6,4,2,8,6,0,3,7,9,5,5,9,8,0,4,8,6,0,8,6,6,1,6,2,7,1,0,2,2,4,0,0,0,4,6,5,5,4,0,1,5,8,3,2,0,9,7,6,2,6,9,9,9,7,1,4,6,2,8,2,5,3,4,5,2,4,4,4,7,2,2,5,3,2,8,2,2,4,9,8,0,9,8,7,6,2,6,7,5,4,7,5,1,0,5,7,8,7,7,8,9,7,0,3,7,7,4,7,2,0,4,1,1,9,1,7,5,0,5,6,6,1,0,6,9,4,2,8,0,5,1,9,8,4,0,3,1,2,4,2,1,8,9,5,9,6,5,3,1,8,9,0,9,8,3,0,9,4,1,1,6,0,5,9,0,8,3,7,8,5]
    # nums2 = [7,8,4,1,9,4,2,6,5,2,1,2,8,9,3,9,9,5,4,4,2,9,2,0,5,9,4,2,1,7,2,5,1,2,0,0,5,3,1,1,7,2,3,3,2,8,2,0,1,4,5,1,0,0,7,7,9,6,3,8,0,1,5,8,3,2,3,6,4,2,6,3,6,7,6,6,9,5,4,3,2,7,6,3,1,8,7,5,7,8,1,6,0,7,3,0,4,4,4,9,6,3,1,0,3,7,3,6,1,0,0,2,5,7,2,9,6,6,2,6,8,1,9,7,8,8,9,5,1,1,4,2,0,1,3,6,7,8,7,0,5,6,0,1,7,9,6,4,8,6,7,0,2,3,2,7,6,0,5,0,9,0,3,3,8,5,0,9,3,8,0,1,3,1,8,1,8,1,1,7,5,7,4,1,0,0,0,8,9,5,7,8,9,2,8,3,0,3,4,9,8,1,7,2,3,8,3,5,3,1,4,7,7,5,4,9,2,6,2,6,4,0,0,2,8,3,3,0,9,1,6,8,3,1,7,0,7,1,5,8,3,2,5,1,1,0,3,1,4,6,3,6,2,8,6,7,2,9,5,9,1,6,0,5,4,8,6,6,9,4,0,5,8,7,0,8,9,7,3,9,0,1,0,6,2,7,3,3,2,3,3,6,3,0,8,0,0,5,2,1,0,7,5,0,3,2,6,0,5,4,9,6,7,1,0,4,0,9,6,8,3,1,2,5,0,1,0,6,8,6,6,8,8,2,4,5,0,0,8,0,5,6,2,2,5,6,3,7,7,8,4,8,4,8,9,1,6,8,9,9,0,4,0,5,5,4,9,6,7,7,9,0,5,0,9,2,5,2,9,8,9,7,6,8,6,9,2,9,1,6,0,2,7,4,4,5,3,4,5,5,5,0,8,1,3,8,3,0,8,5,7,6,8,7,8,9,7,0,8,4,0,7,0,9,5,8,2,0,8,7,0,3,1,8,1,7,1,6,9,7,9,7,2,6,3,0,5,3,6,0,5,9,3,9,1,1,0,0,8,1,4,3,0,4,3,7,7,7,4,6,4,0,0,5,7,3,2,8,5,1,4,5,8,5,6,7,5,7,3,3,9,6,8,1,5,1,1,1,0,3]
    # print len(nums1), len(nums2)
    # print sol.maxNumber(nums1, nums2, 500)
    # print sol.sub_max([1,2,3,2,1],3)
    # print sol.mix_max([3,2,3],[3,4,2])
    # print sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5)
    # print sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5)
    # print sol.maxNumber([6,7], [6,0,4], 5)
    # print sol.maxNumber([8,6,9],[1,7,5],3)
    # print sol.maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15)
    # nums1 = [2,2,0,2,0,1,2,1,2,0,2,2,2,2,1,1,1,1,2,2,0,1,0,1,2,0,1,2,2,2,1,1,0,1,2,2,1,1,1,1,1,0,0,2,1,1,2,0,0,1,0,1,2,0,0,1,0,1,0,2,1,1,1,1,0,0,2,0,2,0,0,0,0,1,2,1,2,2,0,2,1,1,0,2,2,1,0,0,1,2,2,2,2,2,1,2,1,0,1,0,1,1,2,2,0,0,0,1,2,2,0,0,1,2,0,0,1,2,1,0,0,2,0,1,0,0,2,2,2,1,0,1,2,2,2,0,2,0,1,1,1,1,2,0,0,0,1,1,1,2]
    # nums2 = [1,2,1,0,0,1,0,2,0,0,0,2,0,1,1,1,0,0,0,2,2,1,1,1,2,2,2,1,0,2,2,2,0,0,1,2,0,2,2,2,2,1,0,1,1,1,2,2,2,0,1,0,0,1,1,2,1,0,0,0,2,0,2,2,0,0,2,2,2,2,1,0,2,0,1,1,1,0,0,2,1,0,0,2,2,1,0,0,0,1,1,1,0,0,2,1,1,1,0,0,0,1,1,2,0,0,2,2,1,1,0,2,2,0,0,2,1,2,2,1,2,1,2,0,0,0,1,1,2,2,0,0,2,1,0,1,1,1,2,1,1,2,2,1,0,0,0,2,2,2]
    # print len(nums1)
    # print len(nums2)
    # t = time.time()
    # print sol.maxNumber(nums1, nums2, 300)
    # print time.time() - t
    # nums1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # nums2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # print sol.maxNumber(nums1, nums2,100)
    # print sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5)
    # print sol.maxNumber([7,6,1,9,3,2,3,1,1], [4,0,9,9,0,5,5,4,7], 9)
    # nums1 = [1,2,0,1,0,2,2,2,0,2,1,1,1,2,2,0,0,0,2,1,2,1,2,2,0,1,2,1,0,0,0,1,0,0,1,2,1,2,1,1,0,0,2,0,1,0,0,1,2,0,1,2,0,0,2,2,1,2,1,0,0,0,0,1,0,2,0,1,2,1,1,2,1,2,1,1,2,1,2,0,2,1,2,2,0,2,0,0,0,2,0,2,0,1,2,0,1,2,2,0]
    # nums2 = [1,1,0,2,1,0,0,2,2,0,0,2,1,1,1,2,2,1,1,1,1,1,1,2,2,2,1,0,1,1,0,2,0,2,1,1,1,0,2,0,2,1,1,1,2,1,1,2,0,0,1,0,0,2,2,0,0,1,0,2,1,1,1,0,2,2,0,2,0,1,0,1,1,0,1,1,2,1,1,0,2,0,0,0,1,2,1,1,1,0,1,1,1,1,2,1,2,1,2,2]
    # print sol.maxNumber(nums1, nums2, 200)
    # print sol.maxNumber([1,6,5,4,7,3,9,5,3,7,8,4,1,1,4],
    # [4,3,1,3,5,9],
    # 21)
    nums1 = [8,9,7,3,5,9,1,0,8,5,3,0,9,2,7,4,8,9,8,1,0,2,0,2,7,2,3,5,4,7,4,1,4,0,1,4,2,1,3,1,5,3,9,3,9,0,1,7,0,6,1,8,5,6,6,5,0,4,7,2,9,2,2,7,6,2,9,2,3,5,7,4,7,0,1,8,3,6,6,3,0,8,5,3,0,3,7,3,0,9,8,5,1,9,5,0,7,9,6,8,5,1,9,6,5,8,2,3,7,1,0,1,4,3,4,4,2,4,0,8,4,6,5,5,7,6,9,0,8,4,6,1,6,7,2,0,1,1,8,2,6,4,0,5,5,2,6,1,6,4,7,1,7,2,2,9,8,9,1,0,5,5,9,7,7,8,8,3,3,8,9,3,7,5,3,6,1,0,1,0,9,3,7,8,4,0,3,5,8,1,0,5,7,2,8,4,9,5,6,8,1,1,8,7,3,2,3,4,8,7,9,9,7,8,5,2,2,7,1,9,1,5,5,1,3,5,9,0,5,2,9,4,2,8,7,3,9,4,7,4,8,7,5,0,9,9,7,9,3,8,0,9,5,3,0,0,3,0,4,9,0,9,1,6,0,2,0,5,2,2,6,0,0,9,6,3,4,1,2,0,8,3,6,6,9,0,2,1,6,9,2,4,9,0,8,3,9,0,5,4,5,4,6,1,2,5,2,2,1,7,3,8,1,1,6,8,8,1,8,5,6,1,3,0,1,3,5,6,5,0,6,4,2,8,6,0,3,7,9,5,5,9,8,0,4,8,6,0,8,6,6,1,6,2,7,1,0,2,2,4,0,0,0,4,6,5,5,4,0,1,5,8,3,2,0,9,7,6,2,6,9,9,9,7,1,4,6,2,8,2,5,3,4,5,2,4,4,4,7,2,2,5,3,2,8,2,2,4,9,8,0,9,8,7,6,2,6,7,5,4,7,5,1,0,5,7,8,7,7,8,9,7,0,3,7,7,4,7,2,0,4,1,1,9,1,7,5,0,5,6,6,1,0,6,9,4,2,8,0,5,1,9,8,4,0,3,1,2,4,2,1,8,9,5,9,6,5,3,1,8,9,0,9,8,3,0,9,4,1,1,6,0,5,9,0,8,3,7,8,5]
    nums2 = [7,8,4,1,9,4,2,6,5,2,1,2,8,9,3,9,9,5,4,4,2,9,2,0,5,9,4,2,1,7,2,5,1,2,0,0,5,3,1,1,7,2,3,3,2,8,2,0,1,4,5,1,0,0,7,7,9,6,3,8,0,1,5,8,3,2,3,6,4,2,6,3,6,7,6,6,9,5,4,3,2,7,6,3,1,8,7,5,7,8,1,6,0,7,3,0,4,4,4,9,6,3,1,0,3,7,3,6,1,0,0,2,5,7,2,9,6,6,2,6,8,1,9,7,8,8,9,5,1,1,4,2,0,1,3,6,7,8,7,0,5,6,0,1,7,9,6,4,8,6,7,0,2,3,2,7,6,0,5,0,9,0,3,3,8,5,0,9,3,8,0,1,3,1,8,1,8,1,1,7,5,7,4,1,0,0,0,8,9,5,7,8,9,2,8,3,0,3,4,9,8,1,7,2,3,8,3,5,3,1,4,7,7,5,4,9,2,6,2,6,4,0,0,2,8,3,3,0,9,1,6,8,3,1,7,0,7,1,5,8,3,2,5,1,1,0,3,1,4,6,3,6,2,8,6,7,2,9,5,9,1,6,0,5,4,8,6,6,9,4,0,5,8,7,0,8,9,7,3,9,0,1,0,6,2,7,3,3,2,3,3,6,3,0,8,0,0,5,2,1,0,7,5,0,3,2,6,0,5,4,9,6,7,1,0,4,0,9,6,8,3,1,2,5,0,1,0,6,8,6,6,8,8,2,4,5,0,0,8,0,5,6,2,2,5,6,3,7,7,8,4,8,4,8,9,1,6,8,9,9,0,4,0,5,5,4,9,6,7,7,9,0,5,0,9,2,5,2,9,8,9,7,6,8,6,9,2,9,1,6,0,2,7,4,4,5,3,4,5,5,5,0,8,1,3,8,3,0,8,5,7,6,8,7,8,9,7,0,8,4,0,7,0,9,5,8,2,0,8,7,0,3,1,8,1,7,1,6,9,7,9,7,2,6,3,0,5,3,6,0,5,9,3,9,1,1,0,0,8,1,4,3,0,4,3,7,7,7,4,6,4,0,0,5,7,3,2,8,5,1,4,5,8,5,6,7,5,7,3,3,9,6,8,1,5,1,1,1,0,3]
    print sol.maxNumber(nums1, nums2, 500)
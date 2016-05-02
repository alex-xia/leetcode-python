__author__ = 'Qing'
'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''

from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.visited_so_far = set()

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s += '#'
        s = [s[i] for i in range(len(s)) if i < len(s)-1 and s[i] != s[i+1]]
        res = []
        lu = defaultdict(list)
        for i, c in enumerate(s):
            lu[c].append(i)

        def member(beg, end):
            return set(s[beg:end])

        def helper(beg, end, cand):
            if len(cand) == 0:
                return
            # print(s[beg:end], cand)
            for i, c in enumerate(cand):
                inds = lu[c]
                # print('inds=',inds)
                for k in inds:
                    if k < beg:
                        continue
                    if member(k, end) >= set(cand):
                        res.append(k)
                        # print('>>>>>', res, ''.join([s[i] for i in res]))
                        # print(cand, i)
                        del cand[i]
                        helper(k+1, end, cand)
                        return

        helper(0, len(s), sorted(list(set(s))))
        return ''.join([s[i] for i in res])

    def removeDuplicateLetters_wrong(self, s):
        """
        :type s: str
        :rtype: str
        """
        def extract(beg, end):
            extracted = ''
            # visited = set(self.visited_so_far)
            print('@@@@@@@', beg, end, self.visited_so_far)
            for c in s[beg:end]:
                if c in self.visited_so_far:
                    continue
                extracted += c
                # visited.add(c)
            # self.visited_so_far = visited
            return extracted
        print('>>>>>>>', s)
        if len(s) <= 1:
            return s
        lu = defaultdict(list)
        for i, c in enumerate(s):
            lu[c].append(i)
        # print('lu=', lu)
        m, n = min(lu.keys()), max(lu.keys())
        if m == n:
            return m
        p, q = lu[m][0], lu[n][-1]
        res = m+n if p < q else n+m
        self.visited_so_far |= {m, n}
        if p < q:
            mid = extract(p+1, q)
            print('111111mid=',mid)
            if len(mid) > 0:
                mid_res = self.removeDuplicateLetters(mid)
                res = res[0] + mid_res + res[1]
                self.visited_so_far |= {c for c in mid_res}

            right = extract(max(p, q)+1, len(s))
            print('111111right=', right)
            if len(right) > 0:
                right_res = self.removeDuplicateLetters(right)
                res = res + right_res
                self.visited_so_far |= {c for c in right_res}

            left = extract(0, min(p, q))
            print('111111left=', left)
            if len(left) > 0:
                left_res = self.removeDuplicateLetters(left)
                res = left_res + res
                self.visited_so_far |= {c for c in left_res}
        else:
            left = extract(0, min(p, q))
            print('222222left=', left)
            if len(left) > 0:
                left_res = self.removeDuplicateLetters(left)
                res = left_res + res
                self.visited_so_far |= {c for c in left_res}

            right = extract(max(p, q)+1, len(s))
            print('222222right=', right)
            if len(right) > 0:
                right_res = self.removeDuplicateLetters(right)
                res = res + right_res
                self.visited_so_far |= {c for c in right_res}

            mid = extract(q+1, p)
            print('22222mid=',mid)
            if len(mid) > 0:
                mid_res = self.removeDuplicateLetters(mid)
                res = res[0] + mid_res + res[1]
                self.visited_so_far |= {c for c in mid_res}

        print('<<<<<<', res)
        return res

if __name__ == '__main__':
    s = Solution()
    # print(s.removeDuplicateLetters('cbacdcbc'))
    # print(s.removeDuplicateLetters('bcbac'))
    # print(s.removeDuplicateLetters("beeaddbeb"))
    # print(s.removeDuplicateLetters("bbcab"))
    # print(s.removeDuplicateLetters("cbaaa"))
    print(s.removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))


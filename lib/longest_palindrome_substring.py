__author__ = 'Qing'
'''
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def pwidth(i, pw):
            p, q = i-pw-1, i+pw+1
            w = pw
            while p >= 0 and q < len(s) and s[p] == s[q]:
                w += 1
                p -= 1
                q += 1
            return w, i

        def is_p(i, w):
            p, q = i-w, i+w
            while 0 <= p < q < len(s):
                if s[p] != s[q]:
                    return False
                p += 1
                q -= 1
            return True if p==q else False

        s = '|' + '|'.join(list(s)) + '|'
        mid = len(s) // 2
        mw = pwidth(mid, 0)
        for i in range(mid-1, -1, -1):
            if i - mw[0] < 0:
                break
            if is_p(i, mw[0]):
                mw = max(mw, pwidth(i, mw[0]))
        for i in range(mid+1, len(s)):
            if i + mw[0] >= len(s):
                break
            if is_p(i, mw[0]):
                mw = max(mw, pwidth(i, mw[0]))

        return ''.join(s[mw[1]-mw[0]:mw[1]+mw[0]+1].split('|'))

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome_width(i):
            k = 1
            while i-k >= 0 and i+k < len(s) and s[i-k] == s[i+k]:
                k += 1
            return k-1

        def get_repeat_zones():
            zones = []
            beg = end = -1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    beg = i-1 if beg == -1 else beg
                elif end < beg:
                    end = i
                    zones.append((beg, end))
                    beg = end = -1
            if beg != -1 and end == -1:
                zones.append((beg, len(s)))
            return zones

        def add_divider(string, div):
            res = div
            for c in string:
                res += c + div
            return res

        def remove_divider(string, div):
            res = ''
            for c in string:
                if c != div:
                    res += c
            return res

        repeat_zones = get_repeat_zones()
        print(repeat_zones)
        s = add_divider(s, '#')
        print(s)
        pwidth = [-1]*len(s)
        res = ''
        for zone in repeat_zones:
            beg, end = zone
            print('*****',beg,end)
            pwidth[2*beg:2*end+1] = [0] * (2*end-2*beg+1)
            p, q = 2*beg-1, 2*end+1
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p -= 1
                q += 1
            pwidth[beg+end] = (q-p-1)//2
            if pwidth[beg+end] * 2 > len(res):
                res = s[p+1:q]
        print('res=',res,'pwidth=',pwidth)
        return
        for i in range(len(s)):
            if pwidth[i] >= 0:
                continue
            m = palindrome_width(i)
            print('>>>>', i, m, s[i-m:i+m+1], [x for x in zip(range(len(s)),s)])
            if m*2+1 > len(res):
                res = s[i-m:i+m+1]
                print('res=',res)
            pwidth[i] = m
            for j in range(1, m+1):
                mirror_pwidth = pwidth[i-j]
                if j+mirror_pwidth < m:
                    pwidth[i+j] = mirror_pwidth
            print('<<<<<<', pwidth)
        return remove_divider(res, '#')





    def longestPalindrome_slow(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        dp = [(0, set([x for x in range(len(s))])), (1, set([x for x in range(1, len(s))]))]
        res = s[0]
        while len(dp) > 0:
            k, pre = dp[0][0]+2, dp[0][1]
            found = False
            cur = set()
            for j in range(k-1, len(s)):
                print(s[j-k+1:j+1])
                if j-1 in pre and s[j] == s[j-k+1]:
                    found = True
                    cur.add(j)
                    res = s[j-k+1:j+1]
            dp.pop(0)
            if found:
                dp.append((k, cur))
            print(res, dp)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('ccd'))
    # print(s.longestPalindrome('deabcbade'))
    # print(s.longestPalindrome("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))
    # print(s.longestPalindrome('tattarrattat'))
    # print(s.longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"))
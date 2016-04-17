__author__ = 'Qing'

'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        def is_valid_section(sec):
            if len(sec) > 1 and sec[0] == '0':
                return False
            if int(sec) > 255:
                return False
            return True

        def dfs(i, pre):
            if i == len(s) and len(pre) == 4:
                self.res.append('.'.join(pre))
                return
            # lower bound and upper bound sections
            lb = (len(s) - i - 1) // 3 + 1
            ub = len(s) - i
            if len(pre) + lb > 4 or len(pre) + ub < 4:
                return

            for length in [1, 2, 3]:
                if i+length > len(s):
                    break
                sec = s[i:i+length]
                if is_valid_section(sec):
                    cur = list(pre)
                    cur.append(sec)
                    dfs(i+length, cur)

        dfs(0, [])
        return self.res

if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses('25525511135'))
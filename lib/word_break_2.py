__author__ = 'Qing'

'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.memo = {}
        def helper(st):
            if st not in self.memo:
                print('>>>>', st)
                res = []
                for w in wordDict:
                    if st[:len(w)] == w:
                        if len(w) == len(st):
                            res.append(w)
                        else:
                            for pos in helper(st[len(w):]):
                                res.append(w+' '+pos)
                self.memo[st] = res
                print(self.memo[st])
            return self.memo[st]

        return helper(s)

if __name__ == '__main__':
    s = Solution()
    # wordDict = ["cat", "cats", "and", "sand", "dog"]
    # print(s.wordBreak('catsanddog', wordDict))
    sentence = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(s.wordBreak(sentence, wordDict))
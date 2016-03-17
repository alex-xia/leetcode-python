__author__ = 'Qing'
'''
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode('')

    def build_from_arr(self, arr):
        for i in range(len(arr)):
            self.insert(arr[i], i)

    def insert(self, string, i):
        def dfs(node, substr):
            if len(substr) == 0:
                node.children['#'] = TrieNode(str(i))
                return
            c = substr[0]
            if c in node.children:
                child_node = node.children[c]
            else:
                child_node = TrieNode(c)
                node.children[c] = child_node
            dfs(child_node, substr[1:])
        dfs(self.root, string)

    def search(self, string):
        node = self.root
        rem = {}
        for i in range(len(string)):
            c = string[i]
            if '#' in node.children:
                rem[int(node.children['#'].char)] = string[i:]
            if c in node.children:
                node = node.children[c]
            else:
                break
        if '#' in node.children:
            rem[int(node.children['#'].char)] = ''
        return rem

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lu = {w: i for i, w in enumerate(words)}
        print(lu)
        res = {}
        for i, w in enumerate(words):
            print('*****', w)
            for end in range(len(w)+1):
                reverse = w[:end][-1::-1]
                if self.is_palindrome(w[end:]) and reverse in lu:
                    if lu[reverse] != i:
                        if i not in res:
                            res[i] = set()
                        res[i].add(lu[reverse])
                reverse = w[end:][-1::-1]
                print('>>>>', reverse)
                if self.is_palindrome(w[:end]) and reverse in lu:
                    if lu[reverse] != i:
                        if lu[reverse] not in res:
                            res[lu[reverse]] = set()
                        res[lu[reverse]].add(i)
        ret = []
        for left in res:
            for right in res[left]:
                ret.append([left, right])
        return ret

    def palindromePairs_slow(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.res = []
        def bfs(i):
            nxt_cand = []
            for pair in self.cand:
                p, q = pair
                if i == len(words[p]):
                    if self.is_palindrome(words[q][:-i]):
                        self.res.append([p, q])
                    continue
                if i == len(words[q]):
                    if self.is_palindrome(words[p][i:]):
                        self.res.append([p, q])
                    continue
                if words[p][i] == words[q][-i-1]:
                    nxt_cand.append([p, q])
            print('i=',i,'res=',self.res, 'cand=',[[words[x[0]], words[x[1]]] for x in nxt_cand])
            self.cand = nxt_cand
        self.cand = [[x, y] for x in range(len(words)) for y in range(len(words)) if x != y]
        nxt_cand = []
        for pair in self.cand:
            p, q = pair
            if self.cand[p] == self.cand[q][-1::-1]:
                self.res.extend([[p, q], [q, p]])
            else:
                nxt_cand.append(pair)
        self.cand = nxt_cand
        i = 0
        while len(self.cand) > 0:
            bfs(i)
            i += 1
        return self.res

    def palindromePairs2(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie = Trie()
        trie.build_from_arr(words)
        res = []
        def match(i):
            word = words[i]
            rem = trie.search(word[-1::-1])
            for j in rem:
                if j != i and self.is_palindrome(rem[j]):
                    res.append([j, i])
        for i in range(len(words)):
            match(i)
        return res

    @staticmethod
    def is_palindrome(string):
        if len(string) == 0:
            return True
        i, j = 0, len(string)-1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.palindromePairs(["a",""]))
    # words = ["abcd", "dcba", "lls", "s", "sssll"]
    # print(s.palindromePairs(words))
    # print(s.palindromePairs(["bat", "tab", "cat"]))
    # print(s.palindromePairs(["bfdijce","gce","bhgchdcejfcgjfiece","dcebhjhjfgcjdfjg","ejgbjebi","fffgigehhabhfhdge","fajahcagah","ja","ghedcicbg","ccifjedjig","gihbhhebhheecgeifcii","gdjfajdhgibgdb","hcjjdi","jhfjecjigjdhbga","dejbejddhje","ecgfijhcja","ghejidhebg","hfehjfhhfjdjeeahjad","bbajfihihbacdefh","cdeeebaab","cdagiaffffjbjcaia","ab","ejaieca","hcfiecbfcjjhhdj","aehjicd","ieciciiehidbfaaifcj","dca","cjachjbgbefffci","i","j","ejbggahbhii","gjdcjfbhefdgd","ecaed","jbbbjffjgib","biiejcgbcahijgbibiaa","aeahieeceggchd","djicdd","cbj","ggfbeifejd","jgjhehhe","fdgib","ddgabdicbibj","ejbcdfiacicegiibeje","bfdcd","hhjajfgefgefa","cecgbebfchia","jchdbcbh","jcegc","dejfjjcbcdiadaaaei","bjbhfa","ibjba","iddhgdjgjgeid","ifiigfijhad","ahihjcfh","degiedaj","fjfhhiddacjdij","ecjhgc","beebfahffgjaabjafi","fcbdijfjgifjgbijdfc","fc","jgbjajjae","edcgjcigdeecbdhif","fhbhjcbajfddifci","ch","jahggfgdjidhihcafcji","effbcdfbfjdegacdhgc","acjajjbeaeedjbcfihd","bag","ffjdidbghbfdeh","eice","h","aeffjeagfigicadg","hgbejbgcecejfeg","hh","bbadbcbiaechiid","dicajhebdhcgfhgbafa","ehig","eaeddiebehiabf","beijag","gaabbe","gfiehgehe","hffcdfdhcfiia","efbfhe","fdg","hddeaaeacadbhf","dd","hcaicbbjaechebfj","aibjjfdhgchjjhhabe","bjgicf","aij","icaajcfdad","f","fgieaifhghgchhcbjad","gbfjgaabffdeafgejef","bebhbdgjbchbheegba","ceefea","eadjbjfacjeaihefbc","eghihceecbgiehihe","icadjeefhiead","jjibgdb","efedigddjfdea","c","d","hhcjhbdggcbdif","ejhga","fejfbccaeac","ehjbeje","dehd","caddigbdaabdffaie","bjjgjiehaffaachfh","ehhaicejafgddcfihee","jefii","gbijjebhdehi","bfdbcajjfdfh","ca","jbbfibdadiefah","bbefdfcghcaaiijb","ib","ce","bbfdb","cbbcbjebjbjhcfd","ecjge","gjdegighaagbhjc","afdcgdggbi","hdgah","gahdgc","jfbgeaebbd","cefbhfcabagjhjhgeabd","jdaacjjdbc","efacbghiheihedfi","fbffgdcajadjh","aib","ihdcfibgegedeaaa","gehbcj","hjfajbbdc","ihafhfddfhbfgc","fhecfcjd","adefabbggidhgcjf","dedfejiddhcgabfcbihc","hbibhhghhajg","iabjgjihiiiebeig","iegajfg","aaj","gfdhaahdbcbfgja","jd","ifeibdfegjcafdiee","dhjih","afbfdf","gjighgaebb","cbdfjddjfb","aa","gbcajjeajjcfg","gcd","gefddc","fcbiehbiaddcbgfccbid","ifjbgdc","hhgdebcf","iabe","bihj","ifajbhjjhbcd","diabbjjh","bgjhihhgba","jfjcfgbchdfhhggcg","ahdbehfhhccfeefcicf","dghf","dacagebbcieggjjbfi","hejjgdhjbeggedbbgj","a","gghibdbhf","cadfh","fhfbgdegfhccf","hcihffaibjedbjcef","ghhibbgdhgibbfj","jaegfhahhe","fjacga","cjfacjichhhcbhfhbj","gdaejffeiiigfiaci","cdfejfjf","ddf","fhfeifgi","ghghiedhejdhicfhgiaj","abajg","daajgijcdh","bfaiabeaahifjjfdf","ccfhjiegdaj","bhbeegihbifefiia","fb","cjffbhfbgjjfadih","dhefhfaajejee","deijihhhjjibfea","jbgij","agfdidigfeada","daecfjiaacigcjjcb","bgdiied","cjadgiie","ghbhfci","jdbfhhhach","ifiegeaad","eajhiechdhjfhdecfjhe","jhbd","gje","edeggghabeefcaa","aeebiaheefjbigge","bfdhjacgjdficad","fiafgifgajciafiib","aiejhc","gh","eidfbdfcffci","hbdbbcaghejgchiegjf","cdffefdhbfgh","hbjiahfgiiejfcfbg","fdfccabdbggbifhjhjga","dhggbecfhdhcbfddafe","ihee","ciaadifia","gd","hac","dhgaegbichdafdiehe","agdfefdjdbcg","fe","hgdhef","cfgccibbfbcjicg","jj","gdh","decghhbfdcaaiafecaf","jibccbadhdfabjehfi","gaibdjdgjdifcadce","hdcbeegf","ebdaj","fgcdh","hgfabihbhibcdccgd","dhehjgicjhhibfghacig","dgfiagb","jhadfjfafagaggfg","eegg","bjaaeig","chfi","fbb","djcieficibgiiabjdbdc","gdcjijfajgbcb","digh","gbhjcfafhjgchgabjfe","jhggiggjd","eeccgibhheheaaajfadd","bcdcggagb","gbbdbjgi","jchahjcaahbad","bjefigc","ggfhee","ejb","ficidccfgffehdi","iadghjbahjeeja","ighibfegabfegfjafab","dfaeejga","bffbbja","hebbgeigchdb","cfdi","dhha","fjfhfjcabe","gfcca","adeffi","fidgieaijfjcjhgfc","igibid","jjhechdbabegjabdjfc","ai","dgc","aehhchefa","beihbjaahe","ebiagd","bfcafajjahbid","baiijjfgjibafacg","hhajgicga","deadad","efcahgh","aiciffj","hhjchdfeiabfjiiie","agihihabbc","ccacdghah","eifhbbidjbceaegc","hfadbaediajcfbb","jjjjcgeaacffgg","dceiidhcigcbgc","biabjchfi","chgjbhigebba","ciggdgfigbjjjdeccgba","cehe","caidbdi","fjeecdebhidchfeggja","hfbbccad","bbbaggbegaihc","cdahjdjeifccjijdiabj","jcjj","jagf","afagefhgiahebich","fjgejbbdbgab","aih","bgjabhffeafj","fgcghbcheg","ebacdfbchhiaffjgeh","ehhejdbdgg","hafgeiahaffgicafjffi","bbhajadcdeihbggfi","fbdbg","edbiaihc","ed","gcdeefbhidc","gijcigefcecgffjfie","hjg","jahfaghjjbafaebcccf","ahjhafidhbic","gecihhgbhgeeaga","feagfagcef","fhahccbfddhfcaidaa","hajchgjeb","ajhbhfjdfgfdebbgaa","jiedjcgbgifafi","hiaje","cafbaibebabjdadcc","icicefadeecaiceiiaf","jeejjedbfh","ajjdi","diafeaahaeb","heedafafabhcg","hfgdbchbigddjaffg","adahedgichjhhhghg","eajjafcdadbbhfeii","cfachcdbhbcd","fabiigh","gegdbcfghcc","igafadcghfcgbhfccdf","cdbbgbgfggjjedci","ehghd","hgadfefdeeh","ccbeibahfc","jfeag","dihhjehhab","geigahebghifjihdgcfd","fefhbciachhjafj","egdcjbdhgja","fbdfae","cgbdeffbacchjfeig","jgic","caefggbjjdbbjcjfbagb","ddaadegchiejjjbf","ad","dabhgddjgahaach","eddaad","hjbfa","hccejcgcbebfffdhibe","gjababagaaa","ghbjfadjjejaga","cgcdcfadhgdeff","bfihdibecfjehaef","jhijchdaeahdjdfgeac","jb","ejfihbbebihhed","jecgdefeheiebfeabb","aibchhafgcbefdah","dcgefai","fcafbgbfh","gjdaef","eciidjhcbgachbdfjha","dddbccahjdafacjeaib","eifcchejafiijagca","gg","jihahehccafjfdg","dhfia","geghggbdfdgficdhccij","bajjefgdcedjdededd","gdghcgb","bf","gjaeidd","bagc","b","ahaeecafgaafgiif","hfgjbgjicigbciggh","jcfhdgaddbhhgfiebgfi","fejbgcddja","gebjehgdbfhcfidcidhh","ggcaafdbbaiefd","hfaggjab","begicebfhiceicajcfj","iefhaahfajdfchfhecee","icj","cegijjjjfehded","eeadcidaecejchabicbe","ajhhdcachhi","gifibbgaabghj","cajdcfeaefaegdag","bdeedaejj","edjd","ibciabjdefabdgbjgjhi","dhbd","bbijjcjdjjggg","feifjbj","fbdhhahfd","dg","bgeihfafeccibeccjii","gfcecgfebcbgh","jeeefihhaeccf","dgghcbiffdfafjdihai","begae","jbhjbigiceagaigad","acgfbbibihfagih","adgbgjdafcf","gadcjajadeafcabbcg","hfbdfhbcjbdd","hfejjjjbgahcheejef","eihjdcfhbgbcdgdedca","dfg","idfffagdeaee","aejgdiidhbgjaj","cchdbfdaeaaid","igjjaegfe","gedggj","jhbibhehbefddieff","ieaec","ejjifcbdjcjfejcg","djggigibjc","aie"]))
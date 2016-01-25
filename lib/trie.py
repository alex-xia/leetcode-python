__author__ = 'Qing'
'''
Implement a trie with insert, search, and startsWith methods.
'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.children = dict()


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                child = TrieNode()
                child.val = c
                cur.children[c] = child
                cur = child
        leaf = TrieNode()
        cur.children['end'] = leaf


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if 'end' in cur.children:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            # print('c=',c)
            # print('children=', cur.children)
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True




# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
if __name__ == '__main__':
    trie = Trie()
    trie.insert('hello')
    print(trie.search('hel'))
    assert trie.search('hel') == False
    print(trie.search('hello'))
    assert trie.search('hello') == True
    print(trie.startsWith('hel'))
    assert trie.startsWith('hel') == True
    print(trie.startsWith('hele'))
    assert trie.startsWith('hele') == False
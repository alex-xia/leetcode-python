__author__ = 'axia'

'''
 Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
'''

class Node(object):
    def __init__(self, char='^'):
        self.char = char
        self.children = dict()

    def __repr__(self):
        msg = '[' + self.char+']->'
        for c in self.children.keys():
            msg += str(c) + ','
        return msg

class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if c in node.children:
                node = node.children[c]
            else:
                child = Node(c)
                node.children[c] = child
                node = child
        node.children['#'] = Node('#')
        print self.root

    def search(self, word):
        if len(word) == 0:
            return False
        stack = [self.root]
        indexes = [0]
        while len(stack) > 0:
            node = stack.pop()
            i = indexes.pop()
            if i == len(word):
                if '#' in node.children:
                    return True
            else:
                char = word[i]
                if char == '.':
                    for child in node.children.values():
                        stack.append(child)
                        indexes.append(i+1)
                elif char in node.children:
                    stack.append(node.children[char])
                    indexes.append(i+1)
        return False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.add(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    print wordDictionary.search("pattern")
    print wordDictionary.search("word")
    print wordDictionary.search(".or.")

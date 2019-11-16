from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if not word: return
        cur = self.root
        for char in word:
            cur = cur.child[char]
        cur.word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur = self.root

        def helper(cur, word):
            if not word:
                return cur.word
            if word[0] == '.':
                for char in cur.child:
                    if helper(cur.child[char], word[1:]):
                        return True
            elif word[0] in cur.child:
                if helper(cur.child[word[0]], word[1:]):
                    return True
            return False

        return helper(cur, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
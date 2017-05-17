class TrieNode(object):
    def __init__(self, letter, is_terminal=False):
        self.children = dict()
        self.letter = letter
        self.is_terminal = is_terminal

class Trie(object):
    """
    Here “.” can be any letter. this trie is cases-sensitive.
    """
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]
        cur.is_terminal = True

    def search(self, word, node=None):
        cur = node
        if not cur:
            cur = self.root
        for i, letter in enumerate(word):
            # if dot check everyything. This implementation is 
            if letter == ".":
                if i == len(word) - 1: # if last character
                    for child in cur.children.values():
                        if child.is_terminal:
                            return True
                    return False
                for child in cur.children.values():
                    if self.search(word[i+1:], child) == True:
                        return True
                return False
            # if letter
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.is_terminal

t = Trie()
t.addWord("ban")
t.addWord("band")
t.addWord("banana")
t.addWord("bananaz")
print(t.search("and."))
print(t.search(".and"))
print(t.search("ban."))
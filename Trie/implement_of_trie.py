class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if (i not in cur.children):
                cur.children[i] = TrieNode()
            cur = cur.children[i] 
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur= self.root
        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        if cur.end_of_word == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur= self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
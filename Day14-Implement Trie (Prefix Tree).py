#Needs to learn Trie More
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                start[i] = {}
            start = start[i]
        start['$'] = True
 
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                return False
            start = start[i]
        return '$' in start
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start = self.root
        for i in prefix:
            if i not in start:
                return False
            start = start[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
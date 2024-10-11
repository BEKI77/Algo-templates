class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = [ None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root =  TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if not cur.child[ord(i)-ord('a')]:
                cur.child[ord(i)-ord('a')] = TrieNode()
            cur = cur.child[ord(i)-ord('a')]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if not cur.child[ord(i)-ord('a')]:
                return 0
            cur = cur.child[ord(i)-ord('a')]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if not cur.child[ord(i)-ord('a')]:
                return 0
            cur = cur.child[ord(i)-ord('a')]
        return 1

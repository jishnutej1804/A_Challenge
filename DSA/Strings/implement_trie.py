
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end = True

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end

    def startsWith(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))

trie.insert("app")
print(trie.search("app"))
print(trie.startsWith("bat"))

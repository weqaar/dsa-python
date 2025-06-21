class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class SpellChecker:
    def __init__(self):
        self.root = TrieNode()

    def setup(self, list_of_words):
        for word in list_of_words:
            self._insert(word)

    def _insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def isMatch(self, query):
        return self._search(self.root, query, 0)

    def _search(self, node, query, index):
        if index == len(query):
            return node.is_end_of_word

        char = query[index]
        if char == ".":
            for child in node.children.values():
                if self._search(child, query, index + 1):
                    return True
        elif char in node.children:
            return self._search(node.children[char], query, index + 1)

        return False


# Example usage:
spell_checker = SpellChecker()
spell_checker.setup(["cat", "bat", "rat", "drat", "dart", "drab"])

queries = [
    "cat",
    "c.t",
    ".at",
    "..t",
    "d..t",
    "dr..",
    "...",
    "....",
    ".....",
    "h.t",
    "c.",
]
results = {query: spell_checker.isMatch(query) for query in queries}
print(results)

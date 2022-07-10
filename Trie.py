class Node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self, pattern):
        self.pattern = pattern
        self.root = Node()

    def build_trie(self):
        for num in range(len(self.pattern)):
            node = self.root
            pattern_copy = self.pattern[num:]
            for char in pattern_copy:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
        return self.root

    def check(self, text):
        result = True
        node = self.root
        for char in text:
            if char in node.children:
                node = node.children[char]
            else:
                result = False
        return result


root = Trie("panamabananas")
root.build_trie()

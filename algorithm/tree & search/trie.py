# trie algorithm

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


N = int(input())

root = TrieNode()

for _ in range(N):
    word = input()
    current = root
    for char in word:
        if char not in current.children:
            current.children[char] = TrieNode()
        current = current.children[char]
    current.isEnd = True


def dfs(node, depth):
    for char in sorted(node.children):
        print("--" * depth + char)
        dfs(node.children[char], depth + 1)


dfs(root, 0)

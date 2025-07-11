class TrieNode:
    def __init__(self):
        self.children = {}          # Dictionary: character → TrieNode
        self.endOfWord = False      # Flag: is this the end of a complete word?

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()      # Start with empty root node
        

    def insert(self, word: str) -> None:
        cur = self.root                 # Start at root
        for c in word:                  # Process each character
            if c not in cur.children:   # Character path doesn't exist?
                cur.children[c] = TrieNode()  # Create new node
            cur = cur.children[c]       # Move to next node
        cur.endOfWord = True            # Mark end of word



    def search(self, word: str) -> bool:
        cur = self.root                 # Start at root
        for c in word:                  # Follow each character
            if c not in cur.children:   # Path doesn't exist?
                return False            # Word not in trie
            cur = cur.children[c]       # Move to next node
        return cur.endOfWord            # Check if it's a complete word

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root                 # Start at root
        for c in prefix:                # Follow each character
            if c not in cur.children:   # Path doesn't exist?
                return False            # Prefix not in trie
            cur = cur.children[c]       # Move to next node
        return True                     # Found the prefix path
        
        
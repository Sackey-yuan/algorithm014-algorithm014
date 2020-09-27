
from Week_05.practice.testing import TestCode

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for char in word:
            root = root.setdefault(char, {})
        root[self.end_of_word] = self.end_of_word



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for char in word:
            root = root.setdefault(char, {})
            if not root:
                return False
        return self.end_of_word in root

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for char in prefix:
            root = root.setdefault(char, {})
            if not root:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def main():
    test_case = [
                    ]
    tester = TestCode()
    # tester.creat_function(Solution().minPathSum)
    # tester.creat_test_case(test_case)
    # tester.start()
    tester.del_log_cache()


if __name__ == "__main__":
    main()

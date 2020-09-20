from typing import List
class Solution:
    """
    126. 单词接龙 II
    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换后得到的单词必须是字典中的单词。
    说明:

    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:

    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    输出:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]
    示例 2:

    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    输出: []

    解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
    """
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        # n = len(beginWord)
        # def dfs(x,y,bW):
        #     if x == n:
        #         res.append(bW)
        #     eW = "".join(bW[0:x],endWord[x],bW[x+1:])
        #     if eW in wordList:
        #         dfs(x+1,eW)
        #
        # for i in range()
        # dfs(0,beginWord)
        return res
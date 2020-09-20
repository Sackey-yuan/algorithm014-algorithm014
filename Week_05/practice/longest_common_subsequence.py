import functools
from Week_05.practice.testing import TestCode
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # #暴力
        # xl, yl = len(text1), len(text2)
        # @functools.lru_cache(None)
        # def dfs(x, y):
        #     if x ==-1 or y == -1:
        #         return 0
        #     if text2[y] == text1[x]:
        #         return dfs(x-1,y-1) + 1
        #     else:
        #         return max(dfs(x-1, y ), dfs(x, y-1))
        # return dfs(xl-1, yl-1)
        #
        #
        # #使用递归本地超出缓存
        # xl, yl = len(text1), len(text2)
        #
        # @functools.lru_cache(None)
        # def dfs(x,y):
        #     #or wrongly written as and
        #     if x == -1 or y == -1:
        #         return 0
        #     if text1[x] == text2[y]:
        #         return dfs(x - 1, y - 1) + 1
        #     else:
        #         return max(dfs(x - 1, y ), dfs(x, y -1))
        # return dfs(xl - 1, yl - 1)

        n, m = len(text1) + 1, len(text2) + 1
        dp = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if text1[i-1] == text2[j-1]:
                    #忘了+1 5555555555555555555555555555
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    #dp[i][j] 写成了dp[i][i] 5555555555555+1
                    dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
            # print(dp)
        return dp[n-1][m-1]



        # # n, m = len(text1)+1, len(text2)+1
        # # dp = [[0]*m for _ in range(n)]
        # # for i in range(1,n):
        # #     for j in range(1, m):
        # #         if text1[i-1] == text2[j-1]:
        # #             dp[i][j] = dp[i-1][j-1] + 1
        # #         else:
        # #             dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        # # return dp[n-1][m-1]









if __name__ == "__main__":
    testcase = [("fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny",
                "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"),
            ]
    tester = TestCode()
    tester.creat_test_case(testcase)
    tester.creat_function(Solution().longestCommonSubsequence)
    tester.start()
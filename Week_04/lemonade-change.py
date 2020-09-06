class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #优化  180 ms	13.9 MB
        five , ten = 0 , 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five , ten = five -1 , ten +  1
            else:
                if ten > 0 :
                    five,ten = five - 1 ,ten  - 1
                else:
                    five -= 3
            if five < 0 :
                return False
        return True

        #hash map  176 ms	13.9 MB
        # carsh = {5:0 ,10:0 , 20:0}
        # for i in bills:
        #     carsh[i] = carsh.get(i,0) + 1
        #     if i == 10:
        #         if carsh[5]>0:
        #             carsh[5] -= 1
        #         else:
        #             return False
        #     elif i == 20:
        #         if carsh[10] > 0 and carsh[5] > 0:
        #             carsh[10] -= 1
        #             carsh[5] -= 1
        #         elif carsh[5] >= 3 :
        #             carsh[5] -= 3
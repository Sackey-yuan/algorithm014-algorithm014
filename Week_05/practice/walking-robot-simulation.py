from typing import List
class Solution:
    """
    874. 模拟行走机器人
    机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

    -2：向左转 90 度
    -1：向右转 90 度
    1 <= x <= 9：向前移动 x 个单位长度
    在网格上有一些格子被视为障碍物。

    第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

    机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

    返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。



    示例 1：

    输入: commands = [4,-1,3], obstacles = []
    输出: 25
    解释: 机器人将会到达 (3, 4)
    示例 2：

    输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    输出: 65
    解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处


    提示：

    0 <= commands.length <= 10000
    0 <= obstacles.length <= 10000
    -30000 <= obstacle[i][0] <= 30000
    -30000 <= obstacle[i][1] <= 30000
    答案保证小于 2 ^ 31
    """
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #time_complexity：o(n+m) 424 ms	19.4 MB
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        # def moveIndex(n,cur):
        #     if n == -1:
        #         if cur == 0:
        #             return 3
        #         return cur -1
        #     else:
        #         if cur == 3:
        #             return 0
        #         return cur + 1
        x, y, ind , maxd = 0, 0, 0, 0
        obstacleSet = set(map(tuple, obstacles))
        for i in commands:
            if i == -1 :
                ind = (ind -1)%4
            elif i == -2:
                ind = (ind +1)%4
            else:
                for k in range(i):
                    if (x+ d[ind][0],y + d[ind][1] ) not in obstacleSet:
                        x += d[ind][0]
                        y += d[ind][1]
                        # maxd= max(maxd,x*x+y*y) #优化把计算发在移动一次命令的结束位置
                maxd= max(maxd,x*x+y*y)
        return maxd

    def robotSim1(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #模仿最优代码
        xy, obstaclesSet = [(0, 1), (-1, 0), (0, -1), (1, 0)], set(map(tuple,obstacles))
        x, y, res, d = 0, 0, 0, 0
        for cmd in commands:
            if cmd == -1:
                d = (d - 1) % 4
            elif cmd == -2:
                d = (d + 1) % 4
            else:
                i, j = xy[d]
                while cmd and (x + i, y + j) not in obstaclesSet:
                    x += i
                    y += j
                    cmd -= 1
                res = max(res, x ** 2 + y ** 2)
        return res




学习笔记
提交作业格式：
#学号:G20200343110140
#姓名:袁少华
#班级:14期3班
#语言:python
#作业&总结链接:https://github.com/Sackey-yuan/algorithm014-algorithm014/tree/master/Week_01
提交地址：
https://github.com/algorithm014-algorithm014/algorithm014-algorithm014/issues
《14期算法训练营-学员作业批改记录表》
https://shimo.im/sheets/qQWtXYkj8g9WwWX3/8DDj4/ 《14期算法训练营-学员作业批改记录表》

五毒神掌：
1、5-10分钟读题思考，如果没有思路直接看题解，默写代码（自己想着有思路，调试编写很久没有通过怎么办？）
2、紧接着自己尝试写各种解法，体会优化
3、24小时后，再重新做一遍（这时候应该是思维列举方案，并分析优缺点，重点使用最优方案完成提交？）
4、一周后再次做一遍
5、面试前一周恢复性训练

切题四要件：
1、理清题意，明确题目要求
2、尽可能多的列举方案， 分析时间和空间复杂化度
3、尽可能多的动手写代码
4、尝试完毕的测试用例

预习：

周一
climbStairs
1、递归的思维，把求解问题重复的分解为重复的子问题来解决问题
2.找规律的时候在最近的数据中找规律，比如爬楼梯问题，求第n阶的数，换算成n -1，和n-2阶的和
3.现成的有规律的数，可以找数学通项公式
4。多使用python的库函数，计算速度比较快
pow（x,y）计算x的y次幂

周二
twoSum
使用hashmap提高查询速度
周三
plush-one
使用数据类型转换，是最简单清晰的方法
指针遍历和递归的时候增加缓存可以提高速度：



周四
moveZeroes
在数组操作中复制操作比删除添加操作时间复杂度低
两两交换链表中的节点：leetcode-24
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
修改链表的时候应该操作链表的指针 ，而不是修改链表的头

周五：
mergeTwoLists
1.使用递归思路，思路更清晰易懂，每次找到链表中头结点小的链表，然后合并它的next和剩下的链表即可
2.递推的时候，在原有链表上使用指针操作，可以减少空间复杂度，

周日：
双端队列：
测试用例注意：
1、空列表
2、指针越界
收获：
以下函数：
def enTrue(self,n):
        if n < 0:
            n += self._size + 2
        if n > self._size + 1:
            n -= self._size + 2
        #return n
当有return的时：执行enTrue(self._last)，self._last的值没有改变
删除return后传递的参数值修改成功



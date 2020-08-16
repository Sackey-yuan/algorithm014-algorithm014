# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # #迭代法  time_complexity:o(n) space_complexity:o(1) 44 ms 13.6 MB

        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next , a.next ,b.next = b, b.next ,a
            pre = a
        return self.next


        # #递归 time_complexity: o(n) , space_complexity:o(n) 56ms 13.7mb
        # if head == None or head.next == None:
        #     return head
        # per = head.next
        # head.next = self.swapPairs(per.next)
        # per.next = head
        # return per
        
        
        
        
        # # #默写失败 620ms 13.8mb
        # # if not head or not head.next:
        # #     return head
        # # self.next = head.next
        # # head.next = self.next.next
        # # self.next.next = head
        
        # # per, head  = head , head.next
        # # while per.next and per.next.next:
        # #     print('\n1\n',self.next,'\n2\n',per ,'\n3\n',head)
        # #     head.next,per.next , =  head.next.next ,head.next 
        # #     per.next.next = head
        # #     per ,head = head , head.next
        # # return self.next

        
        # # # pre, pre.next = self, head
        # # # while pre.next and pre.next.next:
        # # #     a = pre.next
        # # #     b = pre.next.next
        # # #     pre.next ,a.next ,b.next =  b, b.next ,a
        # # #     pre = a
        # # # return self.next
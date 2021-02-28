# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # return 的链记为l3，初始Node 设为 0， l3指向next3，c为加法产生的进位
        l3 = ListNode(0)
        next3 = l3
        c = 0

        while l1 or l2:
            if l1==None: l1 = ListNode(0)
            if l2==None: l2 = ListNode(0)
        
            next3.val = l1.val+l2.val+c
            c = next3.val // 10
            next3.val = next3.val % 10
            
            l1 = l1.next
            l2 = l2.next

            if l1 or l2 or c:
                 next3.next = ListNode(c)
                 next3 = next3.next
    
        return l3

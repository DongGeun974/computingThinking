# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：2. Add Two Numbers.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-28 오전 12:42 
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum+= l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next

            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

s =Solution()
l1 = [2,4,3]
l2 = [5,6,4]
print(s.addTwoNumbers(l1,l2))
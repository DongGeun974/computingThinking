# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：24. Swap Nodes in Pairs.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-28 오후 6:53 
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur = head
        #
        # while cur and cur.next:
        #     cur.val, cur.next.val = cur.next.val, cur.val
        #     cur = cur.next.next
        #
        # return head

        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next



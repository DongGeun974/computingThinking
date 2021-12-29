# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：328. Odd Even Linked List.py
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head
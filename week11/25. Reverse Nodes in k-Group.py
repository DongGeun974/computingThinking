# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：25. Reverse Nodes in k-Group.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 7:52 
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        count = 0
        current = head
        while current is not None:
            count+=1
            if count%k == 0:
                prev = self.reversList(prev, current.next)
                current = prev.next
            else:
                current = current.next
        return dummy.next

    def reversList(self, start, end):
        prev = start.next
        current = prev.next
        while current is not end:
            nextNode = current.next
            current.next = start.next
            start.next = current
            current = nextNode
        prev.next = end
        return prev

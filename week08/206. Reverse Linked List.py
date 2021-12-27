# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：206. Reverse Linked List.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-28 오전 12:37 
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
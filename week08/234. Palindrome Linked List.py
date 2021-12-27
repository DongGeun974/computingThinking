# -*- coding: UTF-8 -*-
'''
@Project ：week08 
@File ：234. Palindrome Linked List.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-12-28 오전 12:10 
'''


# Definition for singly-linked list.
from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q=deque()
        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

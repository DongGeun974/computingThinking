# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：61. Rotate List.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오후 2:33 
'''


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        lastElement = head
        length = 1

        while lastElement.next:
            lastElement = lastElement.next
            length+=1

        k = k%length

        lastElement.next = head

        tempNode = head

        for _ in range(length-k-1):
            tempNode = tempNode.next

        answer = tempNode.next
        tempNode.next = None

        return answer
# -*- coding: UTF-8 -*-
'''
@Project ：week11 
@File ：19. Remove Nth Node From End of List.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-01-19 오후 5:15 
'''


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        node = head
        while node.next:
            length+=1
            node = node.next

        target = length-n+1
        print(target)
        if target == 1:
            return head.next

        start = 1
        node = head
        pre= head
        while node.next or length ==start:
            if start == length:
                pre.next = None
            if start == target:
                pre.next = node.next
                break
            start+=1
            pre = node
            node = node.next

        return head
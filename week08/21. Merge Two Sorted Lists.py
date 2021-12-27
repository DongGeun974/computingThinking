# -*- coding: UTF-8 -*-
'''
@Project ：week08
@File ：21. Merge Two Sorted Lists.py
@IDE  ：PyCharm
@Author ： Hwang
@Date ：2021-12-28 오전 12:19
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> list[int]:
        # result = []
        # node1, node2 = list1, list2
        # while node1 is not None or node2 is not None:
        #     if node1 is None:
        #         result.append(node2.val)
        #         node2 = node2.next
        #     elif node2 is None:
        #         result.append(node1.val)
        #         node1= node1.next
        #     else:
        #         if node1.val > node2.val:
        #             result.append(node2.val)
        #             node2 = node2.next
        #         else:
        #             result.append(node1.val)
        #             node1 = node1.next
        # return result
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

s=Solution()
n1 = ListNode(4)
n2 = ListNode(2,n1)
n3 = ListNode(1,n2)
n4 = ListNode(4)
n5 = ListNode(3,n4)
n6 = ListNode(1,n5)

print(s.mergeTwoLists(n3,n6))
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1 = 0
        p = 1
        while l1:
            i1 = l1.val * p + i1
            p = p * 10
            l1 = l1.next
        i2 = 0
        p = 1
        while l2:
           i2 = l2.val * p + i2
           p = p * 10
           l2 = l2.next
        i = i1 + i2
        s = str(i)
        length = len(s)
        result = None
        last = None
        for i in range(length):
            if result:
                item = ListNode(int(s[length-i-1]))
                last.next = item
                last = item
            else:
                result = ListNode(int(s[length-i-1]))
                last = result
        return result
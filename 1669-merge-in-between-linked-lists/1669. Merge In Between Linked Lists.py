# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        def p(node):
            bCount = 0
            while node:
                if bCount == b+1: 
                    return node
                else:
                    bCount+=1
                    node = node.next
        target = p(list1)
        print(target)
        diff = b-a
        counter = 1
        curr = list1
        while curr:
            if counter == a:
                curr.next = list2
                while curr.next:
                    curr = curr.next
                curr.next = target
                return list1
            else:
                counter+=1
            curr = curr.next

        
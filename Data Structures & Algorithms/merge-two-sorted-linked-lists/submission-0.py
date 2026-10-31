# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        dummyhead = ListNode(None, None)
        newList = dummyhead
        while curr1 or curr2:
            if curr1:
                if curr2:
                    if curr1.val <= curr2.val: 
                        newList.next = curr1
                        curr1 = curr1.next
                    elif curr2.val < curr1.val:
                        newList.next = curr2
                        curr2 = curr2.next
                else:
                    newList.next = curr1
                    curr1 = curr1.next
            elif curr2:
                newList.next = curr2
                curr2 = curr2.next
            newList = newList.next

        return dummyhead.next

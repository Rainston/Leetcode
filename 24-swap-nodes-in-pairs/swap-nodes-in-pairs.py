# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n=None
        p=None
        cur=head
        while cur and cur.next:
            np=cur.next.next
            temp=cur.next
            cur.next=np
            temp.next=cur
            if p:
                p.next=temp
            else:
                n=temp
            p=cur
            cur=np
        return n


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        k=dum=ListNode()
        while list1 and list2:
          if list1.val<list2.val:
            k.next=list1
            list1,k=list1.next,list1
          else:
            k.next=list2
            list2,k=list2.next,list2
        if list1 or list2:
            k.next=list1 if list1 else list2
        return dum.next
            
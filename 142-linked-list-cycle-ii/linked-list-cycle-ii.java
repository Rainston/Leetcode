/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        int length=0;
        ListNode fast =head;
        ListNode slow=head;
        while(fast!=null &&fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
            if(fast==slow){
                break;
            }
        }
        slow=head;
        if(fast==null ||fast.next==null)return null;
        while(fast!=slow){
            fast=fast.next;
            slow=slow.next;

        }
        return slow;
    }
}
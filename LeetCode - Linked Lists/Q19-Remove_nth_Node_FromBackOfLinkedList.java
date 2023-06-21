/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) 
    {
        ListNode Initial = new ListNode();


            Initial.next = head;
            ListNode Rhead = head;
            ListNode First = Initial;
            ListNode Second = head;
            ListNode Prev = head;
            ListNode SPrev = head;
            ListNode LenthGet = Initial;
            int lenth=0;

            if(head.next == null){return null; }
            
            while(LenthGet.next != null)
            {
                LenthGet = LenthGet.next;
                lenth += 1;

            }
            if(lenth == n){return head.next;}

            if (head.next.next == null){if(n==2){return head.next;}}

            for (int i = 1; i <= n; i++)
            {
                First = First.next;
            }


            while( First.next != null && Prev.next != null )
            {
                Prev = First;
                SPrev = Second;
                First = First.next;
                Second = Second.next;

                System.out.println(Second.val);
                System.out.println(SPrev.val);
            }

            SPrev.next = Second.next;

            return Rhead;

    }
}
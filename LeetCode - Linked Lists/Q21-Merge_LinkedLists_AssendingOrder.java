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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode mergedLL = new ListNode(0);
        ListNode head = mergedLL;
        
        if (list1 == null) { return list2;}
        if (list2 == null) { return list1;}

        while (list1 !=null && list2 != null){
            if (list1.val <= list2.val)
                {
                mergedLL.next = new ListNode(list1.val);
                System.out.println("l1");
                list1 = list1.next;
                }
            else 
                {
                mergedLL.next = new ListNode(list2.val);
                System.out.println("l2");
                list2 = list2.next;
                }
            mergedLL = mergedLL.next;
        }
        if (list1 != null){
            mergedLL.next = list1;
        }else{
            mergedLL.next = list2;
        }

        return head.next;
}}
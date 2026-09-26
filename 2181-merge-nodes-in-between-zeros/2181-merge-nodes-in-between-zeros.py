class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        tail = ans
        cur = head.next
        t = 0
        while cur:
            if cur.val != 0:
                t += cur.val
            else:
                tail.next = ListNode(t)
                tail = tail.next
                t = 0
            cur = cur.next
        return ans.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        c = 0

        while l1 or l2 or c:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + c
            c = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next
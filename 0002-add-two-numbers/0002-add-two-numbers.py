class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        s1, s2 = [], []
        cur1, cur2 = l1, l2
        while cur1 or cur2:
            if cur1:
                s1.append(cur1.val)
                cur1 = cur1.next
            if cur2:
                s2.append(cur2.val)
                cur2 = cur2.next
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        cur = ans
        for i in range(len(s1)):
            if len(s2) > i:
                cur.val += s2[i]
            cur.val += s1[i]
            if i + 1 < len(s1) or cur.val // 10:
                cur.next = ListNode(cur.val // 10)
            cur.val %= 10
            cur = cur.next
        return ans
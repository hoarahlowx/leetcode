class Solution:
    def reverseKGroup(self, node: ListNode | None, k: int) -> ListNode | None:
        ans = node
        while True:
            cur = 1
            head = node
            while cur < k:
                hair = head
                for i in range(k - cur):
                    if hair is None:
                        return ans
                    hair = hair.next
                if hair is None:
                    return ans     
                head.val, hair.val = hair.val, head.val
                cur += 2
                head = head.next
            for i in range(k):
                if node is None:
                    return ans
                node = node.next
        return ans
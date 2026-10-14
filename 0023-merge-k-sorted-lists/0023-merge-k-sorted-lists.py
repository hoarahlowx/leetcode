class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
                
        vals.sort()
        
        ans = ListNode()
        head = ans
        for v in vals:
            head.next = ListNode(v)
            head = head.next
            
        return ans.next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        ans = ListNode()
        head = ans
        while True:
            min_val = float('inf')
            to_move = None            
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < min_val:
                    min_val = lists[i].val
                    to_move = i            
            if to_move is None:
                break                
            head.next = lists[to_move]
            head = head.next            
            lists[to_move] = lists[to_move].next
            
        return ans.next
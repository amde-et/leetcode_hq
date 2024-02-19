class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode() #dummy node

        cur = head
        while cur:
            sortCur = sort
            while sortCur.next and cur.val >= sortCur.next.val:
                sortCur = sortCur.next
                
            tmp, sortCur.next = sortCur.next, cur
            cur = cur.next
            sortCur.next.next = tmp
            
        return sort.next
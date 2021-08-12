# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newhead, last = self.revertk(None, head, k)
        while last:
            curr, last = self.revertk(last, last.next, k)
        return newhead
        
    def revertk(self, prevhead: ListNode, head: ListNode, k: int) -> Tuple[ListNode, ListNode]:
        prev = curr = nex = last = None
        curr = head
        stack = []
        while curr and k > 0:
            k -= 1
            stack.append(curr)
            curr = curr.next
            prev = curr
        last = curr
        if k == 0:
            if prevhead:
                curr = prevhead
            elif len(stack):
                curr = stack.pop()
            head = curr
            while len(stack):
                val = stack.pop()
                curr.next = val
                curr = val
            curr.next = last
            return head, curr
        return head, curr
        
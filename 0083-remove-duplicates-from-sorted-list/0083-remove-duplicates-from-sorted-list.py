# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        prev=head
        if(prev==None):
            return
        nxt = prev.next
        
        while (nxt!=None):
            if prev.val == nxt.val:
                prev.next = nxt.next
                nxt=nxt.next
            else:
                prev=prev.next
                nxt=nxt.next
        return head
        
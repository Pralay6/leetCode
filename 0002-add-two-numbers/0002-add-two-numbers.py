# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        number1=""
        number2=""
        while(l1!=None):
            number1= str(l1.val)+number1
            l1=l1.next
        while(l2!=None):
            number2=str(l2.val)+number2
            l2=l2.next 
        number3=int(number1)+int(number2)
        l1=ListNode(0,None)
        l1.val=number3%10
        number3=number3/10
        l2=l1
        while number3>0:
            l1.next= ListNode(0,None)
            l1=l1.next
            l1.val=number3%10
            number3=number3/10
        return l2
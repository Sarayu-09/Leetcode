

#Logical Deletion method
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def show(self,head):
        t=head
        while t:
            print(t.val,end=" ")
            t=t.next
    def removeElements(self,head,val):
        temp=ListNode(0)#dummy node
        temp.next=head
        prev,curr=temp,head
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return temp.next
obj=Solution()
val=6
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(6)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(4)
head.next.next.next.next.next=ListNode(5)
head.next.next.next.next.next.next=ListNode(6)
head=obj.removeElements(head,val)
obj.show(head)

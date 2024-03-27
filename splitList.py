class ListNode:
    def __init__(self,val=0,next=0):
        self.val=val
        self.next=None
def createL(n):
    for i in range(n):
        v=input("enter v")
        new_node=ListNode(v)
        if i==0:
            head=new_node
        else:
            t=head
            while t.next:
                t=t.next
            t.next=new_node
    return head
def show(head):
    t=head
    while t:
        print(t.val,end="->")
        t=t.next
    
def splitList(head):
    oddhead=head
    evenhead=head.next
    odd=oddhead
    even=evenhead
    while even and even.next:
        odd.next=even.next
        odd=odd.next
        even.next=odd.next
        even=even.next
    odd.next=None
    even.next=None
    print("\nOdd list")
    show(oddhead)
    print("\nEven list")
    show(evenhead)
        
head=createL(int(input("Enter the nodes")))
show(head)
splitList(head)

        

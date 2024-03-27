class ListNode:
    def __init__(self,val=0,next=0):
        self.val=val
        self.next=None
def createL(n):
    for i in range(n):
        v=input("Enter node: ")
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
def splitBranch(head):
    t=head
    cseh,nonch=None,None
    while t:
        if t.val=='CSE':
            if cseh==None:
                cseh=t
                tcse=t
            else:
                tcse.next=t
                tcse=tcse.next
        else:
            if nonch==None:
                nonch=t
                tnon=t
            else:
                tnon.next=t
                tnon=tnon.next
        t=t.next
    tcse.next=None
    tnon.next=None
    print("\nCSE list: ")
    show(cseh)
    print("\nNon-CSE list")
    show(nonch)
head=createL(int(input("Enter the nodes")))
show(head)
splitBranch(head)
    
    
        
    

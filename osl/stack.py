class Node:
    def __init__(self,val):
        self.data=val
        self.next=None


class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,val):
        new=Node(val)
        new.next=self.top
        self.top=new
        self.size+=1


    def pop(self):
        if(self.top==None):
            return -99
        else:
            temp=self.top
            self.top=self.top.next
            n=temp.data
            del temp
            self.size-=1
            return n

    def peek(self):
        if(self.top==None):
            print("Stack is empty")
        else:
            print("The peek is "+ str(self.top.data))

    def display(self):
        temp=self.top
        if(temp==None):
            print("Stack is empty")
        else:
            print("The stack is as follows")
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            
            
ll=Stack()
temp=0
while(temp!=5):
    print("Menu:\n1:Push\n2:Pop\n3:Display\n4:Peek\n5:Exit")
    temp=int(input("Enter your choice"))
    if (temp==1):
        n=int(input("Enter the number to be pushed"))
        ll.push(n)
    elif(temp==2):
        n=ll.pop()
        if(n==-99):
            print("Stack is empty (Can't be popped)")
        else:    
            print ("The value popped is "+str(n))
    elif(temp==3):
        ll.display()
    elif(temp==4):
        ll.peek()



'''
>>> 
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice1
Enter the number to be pushed20
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice1
Enter the number to be pushed30
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice1
Enter the number to be pushed40
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice3
The stack is as follows
40 30 20 Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice2
The value popped is 40
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice2
The value popped is 30
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice2
The value popped is 20
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice2
Stack is empty (Can't be popped)
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice4
Stack is empty
Menu:
1:Push
2:Pop
3:Display
4:Peek
5:Exit
Enter your choice5
>>> 
'''

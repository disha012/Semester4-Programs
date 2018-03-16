class Node:
    def __init__(self,val):
        self.data=val
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert(self,val):
        new=Node(val)
        if(self.head==None):
            self.head=new
            self.tail=new
            self.size=1
        else:
            self.tail.next=new
            self.tail=new
            self.size+=1


    def delete(self,value):
        temp=self.head
        ptr=temp
        while(temp!=None and temp.data!=value):
            
            ptr=temp
            temp=temp.next
        if(temp==None):
            print("Value not found")

        elif(self.head.data==value):
            temp1=self.head
            self.head=self.head.next
            self.size-=1
            del temp1
        elif(self.tail.data==value):
            temp1=self.tail
            temp.next=None
            self.size-=1
            del temp1
        else:
            
            ptr.next=temp.next
            self.size-=1
            del temp

    def display(self):
        temp=self.head
        if(temp==None):
            print("Linked List is empty")
        else:
            print("The list is as follows")
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            
            
ll=LinkedList()
temp=0
while(temp!=5):
    print("Menu:\n1:Insert\n2:Delete\n3:Display\n4:Size\n5:Exit")
    temp=int(input("Enter your choice"))
    if (temp==1):
        n=int(input("Enter the number to be inserted"))
        ll.insert(n)
    elif(temp==2):
        n=int(input("Enter the value to be deleted"))
        ll.delete(n)
    elif(temp==3):
        ll.display()
    elif(temp==4):
        print(ll.size)
        
        

'''
>>> 
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice1
Enter the number to be inserted20
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice1
Enter the number to be inserted30
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice1
Enter the number to be inserted40
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice2
Enter the value to be deleted30
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice3
The list is as follows
20 40 Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice2
Enter the value to be deleted20
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice2
Enter the value to be deleted40
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice3
Linked List is empty
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice4
0
Menu:
1:Insert
2:Delete
3:Display
4:Size
5:Exit
Enter your choice5
>>> 
'''
        

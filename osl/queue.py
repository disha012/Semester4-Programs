class Node:
    def __init__(self,val):
        self.data=val
        self.next=None


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def enqueue(self,val):
        new=Node(val)
        if(self.front==None):
            self.front=self.rear=new
        else:
            self.rear.next=new
            self.rear=new
        self.size+=1


    def dequeue(self):
        if(self.front==None):
            n=-99
            self.size=0
            return n
        elif(self.front==self.rear):
            n=self.rear.data
            self.rear=self.front=None
        else:
            temp=self.front
            self.front=self.front.next
            n=temp.data
            del temp
        self.size-=1
        return n


    def display(self):
        temp=self.front
        if(temp==None):
            print("Queue is empty")
        else:
            print("The queue is as follows")
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            
            
ll=Queue()
temp=0
while(temp!=5):
    print("Menu:\n1:Enqueue\n2:Dequeue\n3:Display\n4:Size\n5:Exit")
    temp=int(input("Enter your choice"))
    if (temp==1):
        n=int(input("Enter the number to be inserted"))
        ll.enqueue(n)
    elif(temp==2):
        n=ll.dequeue()
        if(n==-99):
            print("Queue is empty (No element to be deleted)")
        else:    
            print ("The value deleted is "+str(n))
    elif(temp==3):
        ll.display()
    elif(temp==4):
        print(ll.size)



'''
>>> 
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice1
Enter the number to be inserted20
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice1
Enter the number to be inserted30
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice2
The value deleted is 20
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice2
The value deleted is 30
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice2
Queue is empty (No element to be deleted)
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice4
0
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice3
Queue is empty
Menu:
1:Enqueue
2:Dequeue
3:Display
4:Size
5:Exit
Enter your choice5
>>> 
'''

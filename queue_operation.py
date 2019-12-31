class QueOpe:
    def __init__(self, que, size, front, rear):
        self.que = que
        self.size = size
        self.front = front
        self.rear = rear
        for i in range(0, self.size):
            self.que.append(None)

    def is_empty(self):
        if self.rear == None:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.size-1:
            return True
        else:
            return False

    def enque(self):
        if not self.is_full():
            if self.is_empty():
                self.front = 0
                self.rear = 0
                self.que[self.front] = val
                self.que[self.rear] = val 
                print("\nEnqueued")

            else:
                self.rear += 1
                self.que[self.rear] = val 
                print("\nEnqueued")

        else:
            print("\nThe queue is full.")
    
    def deque(self):
        if not self.is_empty():
            fro_ele = self.que[self.front]
            self.que[self.front] = None
            self.front += 1
            print("\n", fro_ele, " is Dequeued")
        else:
            print("\nQueue is empty to dequeue.")

    def disp(self):
        if not self.is_empty():
            for i in range(self.front, self.rear+1):
                print(self.que[i], end=" ")



front = None
rear = None
que = []
size = int(input("Enter size of queue: "))

qu = QueOpe(que, size, front, rear)


while True:
    print("\n______________________________\n\n\tQUEUE OPERATION\n______________________________\n")
    print("\n\t1. Enqueue\n\t2. Dequeue\n\t3. Display\n\t4. Exit\n")

    ch = int(input("\nYour choice: "))

    if ch == 1:
        if not qu.is_full():
            val = int(input("Value: "))
            qu.enque()
        else:
            print("Queue is full")

    elif ch == 2:
        try:
            qu.deque()
        except:
            print("Oops! No elements to deque.")

    elif ch == 3:
        qu.disp()
    
    elif ch == 4:
        break

    else:
        print("\nEnter valid choice")
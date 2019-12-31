class StackOpe:
    def __init__(self, top, stk, size):
        self.top = top
        self.stk = stk
        self.size = size
        for i in range(0, self.size):
            self.stk.append(None)

    def is_full(self):
        if self.top == self.size-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def push(self):
        self.top = self.top + 1
        self.stk[self.top] = val
        print("Element added")

    def pop(self):
        if self.is_empty() != True:
            pop_ele = self.stk[self.top]
            self.stk[self.top] = None
            self.top = self.top - 1
            print("Element", pop_ele, "is poped")
        else:
            print("No element to pop.")

    def peek(self):
        if self.is_empty() != True:
            print("The peek is : ",self.stk[self.top])
        else:
            print("No element to display")

    def disp(self):
        print("\n\tSTACK ELEMENTS")
        for i in range(self.top+1):
            print(self.stk[i],end=" ")

top = -1
stk = []
size = int(input("Enter size of stack : "))

st = StackOpe(top, stk, size)

while True:
    print("\n______________________________\n\n\tSTACK OPERATION\n______________________________\n")
    print("\n\t1. Push\n\t2. Pop\n\t3. Peek\n\t4. Display\n\t5. Exit\n")

    ch = int(input("\nYour choice: "))

    if ch == 1:
        if not st.is_full():
            val = int(input("Value: "))
            st.push()
        else:
            print("Stack Overflow")

    elif ch == 2:
        st.pop()

    elif ch == 3:
        st.peek()

    elif ch == 4:
        st.disp()
    
    elif ch == 5:
        break

    else:
        print("\nEnter valid choice")
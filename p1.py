# rep1
q = []

def Enqueue():
    if len(q) == size:   # check whether the queue is full or not
        print("Queue is Full!!!!")
    else:
        element = input("Enter the element: ")
        q.append(element)
        print(element, "is added to the Queue!")

def dequeue():
    if not q:   # or if len(q) == 0
        print("Queue is Empty!!!")
    else:
        e = q.pop(0)
        print("Element removed!!:", e)

def display():
    print("Queue elements are:", q)


size = int(input("Enter the size of Queue: "))

while True:
    print("\nSelect the Operation: 1.Add 2.Delete 3.Display 4.Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid Option!!!")

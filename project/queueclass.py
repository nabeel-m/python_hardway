class Queue:
    def __init__(self):
       self.items =  []
        
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
        

def main():
    q = Queue()
    q.items =  ['akbar','ajmal','arjun','ajay']
    
    print(q.items)
    print("size",q.size())
    print("\n1.ENQUEUE\n2.DEQUEUE")
    
    op = int(input("Choice"))
    
    if op == 1:
        q.enqueue(input("Data :"))
        print("items after Enque :",q.items)
        print("queue size :",q.size())

    if op == 2:
        print("Deleted item :",q.dequeue())
        print("items after Dequeue :",q.items)
        print("queue size :",q.size())

if __name__ == "__main__":
    main()

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        

def main():
    s = Stack()
    s.items = ['akbar','ajmal','arjun','ajay']
    
    print("Size :",s.items)
    print("\n1.PUSH\n2.POP")
    
    op =int(input("Choice :"))
    
    if op == 1:
        s.push(input("Data :"))
        print("items after push operation :",s.items)
        print("Stack size :",s.size())

    if op == 2:
        print("Deleted item :",s.pop())
        print("Stack after pop operation:",s.items)
        print("Stack size:",s.size())

if __name__ == "__main__":
    main()





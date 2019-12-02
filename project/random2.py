class Filter:
    def __init__(self, size, threshold):
        self.items = []
        self.size = size
        self.threshold = threshold

    def filter(self, threshold):
        for i in range(len(self.items)):
            if self.items[i] <= self.threshold: 
                return self.items.remove(self.items[i])  

    #def display(self, size, threshold):
     #   print(self.items[len(self.items)-self.size:]

def main():
    s = int(input("Size:"))
    t = int(input("Threshold:"))
    
    f = Filter(s,t)
    f.items = [20, 30, 40, 50, 70, 100]
    print(f.items)
    
    print("\n")
    
    if (s <= len(f.items)):
        for i in range(len(f.items)):
            f.filter(t)
        print(f.items[len(f.items)-s:])
    else:
        for i in range(len(f.items)):
            f.filter(t)
        print(f.items[:])

            

    print("\n") 
    

 
if __name__ == "__main__":
    main()

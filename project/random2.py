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
    f.items = [25, 10, 30, 37, 50, 11]
    
    print(f.items)
    print("\n")
    
    for i in range(len(f.items)):
        f.filter(t)
    #f.items.sort()
    print(f.items[len(f.items)-s:])

if __name__ == "__main__":
    main()

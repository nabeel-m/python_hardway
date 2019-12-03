class Filter:
    def __init__(self, size, threshold):
        self.items = []
        self.size = size
        self.threshold = threshold

    def filter(self, size, threshold):
        for i in range(len(self.items)-1,-1,-1):
            if self.items[i] <= self.threshold: 
                self.items.remove(self.items[i])
                
        return self.items[len(self.items)-self.size:]

def main():
    s = int(input("Size:"))
    t = int(input("Threshold:"))
    
    f = Filter(s,t)
    f.items = [25, 10, 30, 37, 50, 11]
    
    print(f.items)
    print("\n")
    print(f.filter(s,t))

if __name__ == "__main__":
    main()

class Random:
    def __init__(self,size):
        self.data = []
        self.size = size

    def add(self,data):
        self.data.append(data)

    def display(self,data):
        print(self.data)

        
def main():
    s = int(input("How Many last digits:"))
    r= Random(s)
    r.data = []
    l = int(input("size of array :"))

    for i in range(1,l+1):
        r.add(i)

    r.display(i)
    print("\n") 
    print(f"Last {s} digits:\n")   
    print(r.data[len(r.data)-s:len(r.data)])

if __name__ == "__main__":
    main()

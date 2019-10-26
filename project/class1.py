class Shark:
    def __init__(self,name):
        self.name=name
    def swim(self):
        print(self.name +" is swimming")

    def be_awesome(self):
        print(self.name +" is awesome")    

def main():
    bullshark=Shark("Bullshark")
    bullshark.swim()
    bullshark.be_awesome()  

if __name__=="__main__":
    main()            
class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover=Dog("rover")

satan =Cat("satan")

mary =Person("mary")

mary.pet = satan

frank = Employee("frank",120000)

frank.pet = rover

flipper = Fish()

crouse = salmon()

hary= Halibut()



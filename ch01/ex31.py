class Parent(object):

    def implicit(self):
        print("parentimplicit()")

class Child(Parent):
        pass

dad=Parent()
son=Child()

dad.implicit()
son.implicit()

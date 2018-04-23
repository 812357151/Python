class Parent:
    parentTitle="this a parent"
    def __init__(self,name):
        self.parentTitle+=name
    def printParentTitle(self):
        print(self.parentTitle)
    def __del__(self):
        print(self.__class__.__name__)

class Child(Parent):
    childName="this a child"
    def __init__(self,name):
        Parent.__init__(self,name)
        self.childName+=name
    def printChildTitile(self):#1122
        print(self.childName)


dchild=Child("aaass")
dchild.printChildTitile()
dchild.printParentTitle()
print(Parent.parentTitle)
del dchild
print(Parent.parentTitle)
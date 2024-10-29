class Grandparent:
    def __init__(self, name):
        self.name = name
    
    def show_grandparent(self):
        print(f"Grandparent Name: {self.name}")

class Parent(Grandparent):
    def __init__(self, name, parent_name):
        super().__init__(name)  
        self.parent_name = parent_name
    
    def show_parent(self):
        print(f"Parent Name: {self.parent_name}")

class Child(Parent):
    def __init__(self, name, parent_name, child_name):
        super().__init__(name, parent_name)  
        self.child_name = child_name
    
    def show_child(self):
        print(f"Child Name: {self.child_name}")

child_instance = Child("Grandpa ganesan", "Dad dhamodharan", "Son dharani")

child_instance.show_grandparent()  
child_instance.show_parent()    
child_instance.show_child()

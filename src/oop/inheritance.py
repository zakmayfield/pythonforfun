from classes import TestClass

class ChildClass(TestClass):
    def __init__(self, param1, param2, param3) -> None:
        super().__init__(param1, param2)
        self.param3 = param3

    def method_three(self):
        return self.param3
    
test_child = ChildClass('child param1', 'child param2', 'child param3')

one = test_child.method_one()
two = test_child.method_two()
three = test_child.method_three()

print(one, two, three)
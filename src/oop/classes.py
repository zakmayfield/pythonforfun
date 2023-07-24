
class TestClass:
    def __init__(self, param1, param2) -> None:
        self.param1 = param1
        self.param2 = param2

    def method_one(self):
        return self.param1

    def method_two(self):
        return self.param2
    

test_object = TestClass('param number one', 'param two')

one = test_object.method_one()
two = test_object.method_two()

print(one, two)
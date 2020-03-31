"""
Learning how to write a clean_code
"""
class MyClass():
    """
    This is an example to write a class
    with a docstring
    """
    def __init__(self, greet):
        self.greet = greet
    #end_init()
    def __repr__(self):
        return 'a custom object (%r)' % (self.greet)
    #end_repr()

PYOBJECT = MyClass("Bidoof")
print(PYOBJECT)

class Employee(object):
    """This is class for employee"""
    numEmployee = 0

    def __init__(self, name, rate):
        """Assign init's parameters to the object self"""
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1
    #end_init()

    def __del__(self):
        """Delete the number of employee"""
        Employee.numEmployee -= 1

    def hours_work(self, num_hours):
        """Calculate how many hours employee work"""
        self.owed = num_hours * self.rate
        return "%.2f hours worked" % num_hours
    #end_hours_work()

def lazy(number):
    """Return arg in binner form """
    temp = []
    while number != 0:
        print(f'{number} mod 2 : {number % 2}')
        temp.append(number % 2)
        number = int(number/2)
    #end_while()

    temp.reverse()
    print(temp, end="\n\n")
    print("The answer : ", end="")
    temps = 1
    for digit in temp:
        binner = str(str(digit) + " ") if(temps % 8 == 0) else str(digit)
        print(binner, end="")
        temps += 1
    #end_for()

    print(f'\n{lazy.__doc__}')

print("")
lazy(22139592)
print("")

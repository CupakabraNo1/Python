class Person:

    class_parameter = 0

    def __init__(self, name):
        self.role = 1
        self.name = name
        Person.class_parameter += 1

    def __str__(self):
        return "Person with name {} and role {}".format(self.name, self.role)

    def __del__(self):
        del self


class Worker(Person):
    
    def __init__(self, name, salary):
        super(Worker, self).__init__(name)
        self.salary = salary

    def __str__(self):
        return super(Worker, self).__str__() + "and salary of {}".format(self.name, self.role, self.salary)

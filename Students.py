class Human(object):
    def __init__(self):
        self._name = "John"

    def speak(self):
        print('Gday')


class Student(Human):
    def __init__(self):
        super(Student, self).__init__()

    def speak(self):
        Human.speak(self)


s = Student()
h = Human()
print(s._name)
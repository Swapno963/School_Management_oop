import random
class Person:
    def __init__(self,name) -> None:
        self.name = name


class Techer(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def teach(self):
        pass

    def take_exam(self, students):
        for student in students:
            marks = random.randint(0,100)
        #todo : set marks for the suject for each student

    def __repr__(self) -> str:
        print(f"\n{self.name} ")


class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.grade = None

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id = value

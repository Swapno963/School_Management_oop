class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        #composition
        self.classrooms = {}


    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self,student):
        if student.classroom in self.classrooms:
            #set student id
            self.classrooms[student.classroom].add_student(student)
        else:
            print(f'\nNo classroom as named {student.classroom}')


    def __repr__(self) -> str:
        print(f"\n-----------ALL CLASSROOMS ------------")
        count =0
        for key, value in self.classrooms.items():
            print("\t",count, "\t",key)
            count += 1

        print("\n----------Students------------") 
        eight = self.classrooms['eight']
        for student in eight.students:
            print("\t",student.name)
        return ''
    
            

class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name
        #composition
        self.students = []
        self.subjects = []


    def add_student(self,student):
        serial_id = f'{self.name}-{len(self.students)}'
        student.id = serial_id
        self.students.append(student)
        
    def add_subject(self,subject):
        self.subjects.append(subject)

    def __str__(self):
        return f'{self.name}-{len(self.students)}'
    


class Subject:
    def __init__(self,name,max_mark,pass_mark,techer) -> None:
        self.name = name
        self.max_mark = max_mark
        self.pass_mark = pass_mark
        self.teacher = techer

    def __repr__(self) -> str:
        print(f'Name : {self.name} Pass mark : {self.pass_mark}')
        return ''
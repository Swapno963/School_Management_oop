from School import School,ClassRoom,Subject
from Persons import Student, Techer

def main():
    school = School('Adam jee','u tt ra')

    eight = ClassRoom('eight')
    school.add_classroom(eight)

    nine = ClassRoom('nine')
    school.add_classroom(nine)

    # creating sutdent
    abul = Student('Abir khan',eight)
    School.student_admission(abul)

    babul = Student('babul khan',eight)
    School.student_admission(babul)
    
    cabul = Student('Acabulkhan',eight)
    School.student_admission(cabul)

    

    #creating teacher
    physics_techer = Techer('Shajahan Khan')
    chemistry_techer = Techer('Chemihan Khan')

     #creating subjects
    physics = Subject('physics',100,33,physics_techer)
    chemistry = Subject('chemistry',100,33,chemistry_techer)
    
    eight.add_subject(physics)
    eight.add_subject(chemistry)


if __name__ == '__main__':
    main()
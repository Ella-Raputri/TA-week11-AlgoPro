from courses import Course
from students import Student
import matplotlib.pyplot as plt

#test student class
with open('myStudents.txt',"w") as f:
    f.writelines('STUDENTS INFORMATION')

student1 = Student("Ella", 18, '001')
student2 = Student("Mary", 18, '002')
student3 = Student("Ann", 18, '003')
student4 = Student("Rene", 18, '004')
student5 = Student("Cater", 18, '005')

student5.set_name('Mamere')
student2.set_student_ID('006')
student5.display_student_info()


#test course class
print('\n\n=======TEST COURSE CLASS==========\n')

with open('myCourses.txt',"w") as f:
    f.writelines('COURSES INFORMATION\n')

course1 = Course('MATH1','Discrete Math', 'Lyris', '4', '4')
course2 = Course('COMP1','AlgoPro', 'Alain', '10', '4')
course3 = Course('CHAR1','Pancasila', 'Narcissus', '8', '2')

course1.set_title('DisMath')

course3.register_student(student5)
course3.register_student(student1)
course2.register_student(student5)
course2.register_student(student1)
course2.remove_student(student5)

course1.register_student(student1)
course1.register_student(student2)
course1.register_student(student3)
course1.register_student(student4)
course1.register_student(student5)

print(student1.get_courses_name_enrolled())
print(course1.check_available_slot())
student5.display_student_info()

course1.display_course_students()
course1.display_course_details()


#chart number of course for each student
student_name = [student1.get_name(), student2.get_name(), student3.get_name(), student4.get_name(), student5.get_name()]
number_of_course = [len(student1.get_courses_enrolled()), len(student2.get_courses_enrolled()), len(student3.get_courses_enrolled())
                    , len(student4.get_courses_enrolled()), len(student5.get_courses_enrolled())]

plt.plot(student_name, number_of_course, "o--r")

plt.title("Number of Course that Each Student Participate")
plt.xlabel("Student's name")
plt.ylabel("Number of Course(s)")
yint = [0,1,2,3,4,5]
plt.yticks(yint)

plt.grid(True)
plt.show()


#chart number of students in each course
courses_title = [course1.get_title(), course2.get_title(), course3.get_title()]
current_student = [course1.get_current_students(), course2.get_current_students(), 
                   course3.get_current_students()]
plt.yticks(yint)
plt.bar(courses_title, current_student)
plt.show()

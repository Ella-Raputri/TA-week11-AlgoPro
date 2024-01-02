class Course:

    def __init__(self, course_code, title, lecturer, maximum_capacity, scu):
        self.__course_code = course_code
        self.__title = title
        self.__maximum_capacity = int(maximum_capacity)
        self.__current_students = 0
        self.__lecturer = lecturer
        self.__scu = scu
        self.__students = []
        self.file = "myCourses.txt"

        #write course details to a file
        f = open(self.file, 'at')	
        f.writelines("Course Details")
        f.writelines("\n=============================================================")
        f.writelines(f"\nCourse Code: {self.__course_code}")
        f.writelines(f"\nCourse Name: {self.__title} (current students: {self.__current_students})")
        f.writelines(f"\nCourse Maximum Capacity: {self.__maximum_capacity}")	 	
        f.writelines(f"\nCourse Lecturer: {self.__lecturer}")	
        f.writelines(f"\nCourse SCU: {self.__scu}\n\n")	
        f.close()				
       

    #getters
    def get_course_code(self):
        return self.__course_code
    def get_title(self):
        return self.__title
    def get_maximum_capacity(self):
        return self.__maximum_capacity
    def get_current_students(self):
        return self.__current_students
    def get_lecturer(self):
        return self.__lecturer
    def get_scu(self):
        return self.__scu
    
    #replace lines in file
    def replace(self, old, new):
        with open(self.file,"r") as f:
            newline=[]
            for word in f.readlines():        
                newline.append(word.replace(old,new))

        with open(self.file,"w") as f:
            for line in newline:
                f.writelines(line)


    #setters
    def set_title(self,title):
        self.replace(f"Course Name: {self.__title}", f"Course Name: {title}")
        self.__title = title
    def set_maximum_capacity(self,maximum_capacity):
        self.replace(f"Course Maximum Capacity: {self.__maximum_capacity}\n", f"Course Maximum Capacity: {int(maximum_capacity)}\n")
        self.__maximum_capacity = int(maximum_capacity)
    def set_lecturer(self, lecturer):
        self.replace(f"Course Lecturer: {self.__lecturer}\n", f"Course Lecturer: {lecturer}\n")
        self.__lecturer = lecturer
    

    def register_student(self, student):
    #student can only register in the course if the course is still not full and the student is not registered yet in the course
        if self.__current_students >= self.__maximum_capacity:
            print(f"Registration failed for {student.get_name()}. The course has reached its maximum capacity.")
        elif student in self.__students:
            print(f"Registration failed for {student.get_name()}. The student has enrolled in the course.")
        else:
            self.replace(f"Course Name: {self.__title} (current students: {self.__current_students})\n", f"Course Name: {self.__title} (current students: {int(self.__current_students)+1})\n")
            self.__students.append(student)
            self.__current_students += 1

            (student.get_courses_enrolled()).append(self)
            student.replace(f"Name: {student.get_name()}", f"Name: {student.get_name()} ({self.__title})") 

    
    def remove_student(self, student):
    #student is removed if the student has registered on the course
        if student not in self.__students:
            print(f"Removing failed for {student.get_name()}. The student does not participate in this course.")
        else:
            self.replace(f"Course Name: {self.__title} (current students: {self.__current_students})\n", f"Course Name: {self.__title} (current students: {int(self.__current_students)-1})\n")
            self.__current_students -= 1
            self.__students.remove(student)

            (student.get_courses_enrolled()).remove(self)
            with open(student.file,"r") as f:
                newline=[]
                for word in f.readlines():
                    if student.get_name() in word:        
                        newline.append(word.replace(word,f"Name: {student.get_name()}\n"))
                    else:
                        newline.append(word)

            with open(student.file,"w") as f:
                for line in newline:
                    f.writelines(line)
            
            for title in student.get_courses_name_enrolled():
                student.replace(f"Name: {student.get_name()}", f"Name: {student.get_name()} ({title})")
                      

    def check_available_slot(self):
        return self.__maximum_capacity - self.__current_students

    def display_course_details(self):
        print("\nCourse Details")
        print('=============================================================')
        print(f"Course Code: {self.__course_code}")
        print(f"Course Name: {self.__title}")
        print(f"Course Maximum Capacity: {self.__maximum_capacity}")
        print(f"Current Number of Students Enrolled: {self.__current_students}")
        print(f"Course Available Slots: {self.check_available_slot()}")
        print(f"Course Lecturer: {self.__lecturer}")
        print(f"Course SCU: {self.__scu}")

    def display_course_students(self):
        print(f'\nCourse Students for {self.__title}')
        print('=============================================================')
        for i in range (0,self.__current_students):
            print(f"{i+1}. {self.__students[i].get_name()}")


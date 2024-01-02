class Student:

    def __init__(self, name, age, student_ID):
        self.__name = name
        self.__age = int(age)
        self.__student_ID = student_ID
        self.__courses_enrolled = []
        self.file = 'myStudents.txt'

        #write students detail to a file
        f = open(self.file, 'at')
        f.writelines("\n=============================================================")
        f.writelines(f"\nName: {self.__name}")
        f.writelines(f"\nAge: {self.__age}")	
        f.writelines(f"\nStudent ID: {self.__student_ID}")	
        f.close()
    
    #getters
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_student_ID(self):
        return self.__student_ID
    def get_courses_enrolled(self):
        return self.__courses_enrolled
    def get_courses_name_enrolled(self):
        return [item.get_title() for item in self.__courses_enrolled]
    
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
    def set_name(self, name):
        self.replace(f"Name: {self.__name}", f"Name: {name}")
        self.__name = name
    def set_student_ID(self, student_ID):
        self.replace(f"Student ID: {self.__student_ID}\n", f"Name: {student_ID}\n")
        self.__student_ID = student_ID

    
    def display_student_info(self):
        print('\nStudent Information')
        print('================================================================')
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Student ID: {self.__student_ID}")
        print(f"Courses Enrolled: ", end="")
        if len(self.__courses_enrolled) == 0: 
            print('[]')
        else:
            for i in range(0, len(self.__courses_enrolled)):
                if i == (len(self.__courses_enrolled)- 1):
                    print(f"{self.__courses_enrolled[i].get_title()}")
                else:
                    print(f"{self.__courses_enrolled[i].get_title()}", end=", ")
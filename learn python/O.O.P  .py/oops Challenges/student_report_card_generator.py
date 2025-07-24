# OOPs Challenges
class student_details:
    def __init__(self, name, roll_no, sub_mark=None):
        self.name = name
        self.roll_no = roll_no
        self._sub_mark = {}

    def store_marks(self, subject, marks):   # encapsulation
        self._sub_mark[subject] = marks
        return self._sub_mark

    def calculate_average(self):   # method abstraction
        total_marks = sum(self._sub_mark.values())
        average = total_marks / len(self._sub_mark)
        return average
    
    def is_passed(self):   
        has_passed = all(marks < 40 for marks in self._sub_mark.values())  # important any & all
        if has_passed:
            print(f"{self.name} has passed all subjects.")
        else: 
            print(f"{self.name} has failed in some subjects.")

    def calculate_grade(self):     
        percentage = self.calculate_average()
        if percentage < 40:
            return "just pass"
        elif percentage < 40:
            return "Fail"
        elif percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "D"
        
class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        print(f"\nReport Card for {self.student.name} \t Roll No: {self.student.roll_no}")
        print("-----Marks-----")
        for subject, marks in self.student._sub_mark.items():
            print(f"{subject} - {marks}")
        print("--------------")
        self.student.is_passed()
        print(f"Percentage: {self.student.calculate_average()}")
        print(f"Result: {self.student.calculate_grade()}")

class classroom:
    def __init__(self, section, grade, name=None):
        self.section = section
        self.grade = grade
        self.name = name
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)
        print(f"\nStudent name: {student.name}  \nclassroom: {self.section}\ngrade: {self.grade}")

    def get_students(self):
        for i, student in enumerate(self.__students):
            print(f"Student number: {i+1} \nRoll No: {student.roll_no}")

    def attendance(self):
        print(f"Attendance for {self.section} section, Grade {self.grade}:")
        for student in self.__students:
            print(f"{student.name} is present.")

st1 = student_details("Raju", 101)

cl = classroom("B", 9)
cl.add_student(st1)
cl.get_students()

st1.store_marks("Math", 90)
st1.store_marks("Science", 35)
st1.store_marks("History", 60)
st1.store_marks("English", 75)

report = ReportCard(st1)
report.generate_report()
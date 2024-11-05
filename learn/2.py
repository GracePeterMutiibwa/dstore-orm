class Student:
    name = None

    regno  = None

    def __init__(self, studentName, studentRegno):
        self.name = studentName

        self.regno = studentRegno


studentOne = Student('bless', '5252525')

studentTwo = Student('Believe', '5363535')
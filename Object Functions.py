from Student import Student

student1 = Student('Oscar', 'Accounting', 3.1)
student2 = Student('Phyllis', 'Bussiness', 3.8)

def on_honor_role(self):
    if self.gpa >= 3.5:
        return True
    else:
        return False
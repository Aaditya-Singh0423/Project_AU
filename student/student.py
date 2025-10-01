class Students:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f"Name:{self.name}\nRollno:{self.rollno}\nMarks:{self.marks}")
if __name__=="__main__":
    s1=Students("Chirag",1,100)
    s1.display()
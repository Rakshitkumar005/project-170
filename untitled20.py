from tkinter import *
root = Tk()

root.title("% Calculation")
root.geometry("600x600")

grade_3_label = Label(root)
grade_4_label = Label(root)
grade_5_label = Label(root)

class grade_3():
    
    def __init__(self, language_arts, maths):
        self.language_arts = language_arts
        self.maths = maths
        
    def percentage(self):
        total_marks = self.language_arts + self.maths
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100 / 200
        grade_3_label["text"] = grade_3_percentage
        
class grade_4():
    
    def __init__(self, language_arts, maths, sst):
        self.language_arts = language_arts
        self.maths = maths
        self.sst = sst
        
    def percentage(self):
        total_marks = self.language_arts + self.maths + self.sst
        total_marks_with_100 = total_marks * 100
        grade_4_percentage = total_marks_with_100 / 300
        grade_4_label["text"] = grade_4_percentage
        
class grade_5():
    
    def __init__(self, language_arts, maths, sst, foreign_language):
        self.language_arts = language_arts
        self.maths = maths
        self.sst = sst
        self.foreign_language = foreign_language
        
    def percentage(self):
        total_marks = self.language_arts + self.maths + self.sst + self.foreign_language
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100 / 400
        grade_5_label["text"] = grade_5_percentage
        
obj_grade_3 = grade_3(40, 50)
grade_3_btn = Button(root, text = "Grade - 3", command = obj_grade_3.percentage)
grade_3_btn.pack(padx = 20, pady = 20)
grade_3_label.pack(padx = 20, pady = 20)

obj_grade_4 = grade_4(40, 50, 90)
grade_4_btn = Button(root, text = "Grade - 4", command = obj_grade_4.percentage)
grade_4_btn.pack(padx = 20, pady = 20)
grade_4_label.pack(padx = 20, pady = 20)

obj_grade_5 = grade_5(40, 50, 70, 90)
grade_5_btn = Button(root, text = "Grade - 5", command = obj_grade_5.percentage)
grade_5_btn.pack(padx = 20, pady = 20)
grade_5_label.pack(padx = 20, pady = 20)

root.mainloop()


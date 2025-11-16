# Build a Simple Student Grade Calculator that takes marks and returns grade (A, B, C, etc.) with encouraging messages for each grade

def grading_system(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = float(input("Enter your marks: "))
grade = grading_system(marks)
print(f"Your grade is {grade}.")

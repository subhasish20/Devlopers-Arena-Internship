def student_grade_calculator():
    print("Student Grade Calculator")
    marks = float(input("Enter your marks (0-100): "))

    if marks >= 90:
        grade = "A"
        message = "Excellent work!"
    elif marks >= 80:
        grade = "B"
        message = "Great job!"
    elif marks >= 70:
        grade = "C"
        message = "Good effort!"
    elif marks >= 60:
        grade = "D"
        message = "You can do better!"
    else:
        grade = "F"
        message = "Sorry, you failed. Don't give up, keep trying!"

    print(f"Your grade is: {grade}")
    print(message)

student_grade_calculator()

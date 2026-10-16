

uni_name = "AWKUM"
passing_marks = 40

subjects = ("Math", "Science", "English")

students = ["Ali", "Ahmed", "Sara"]

courses = {"Python", "Python", "Java", "Java", "AI"} 


def check_result(marks):
    
    if marks >= 80:
        return "A Grade"
    elif marks >= 60:
        return "B Grade"
    elif marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"
print(f"College: {uni_name}")
print(f"Subjects: {subjects}")
print(f"Courses Available: {courses}")

for name in students:  
    marks = int(input(f"Enter marks for {name}: "))
    grade = check_result(marks) 
    print(f"{name} -> {grade}")


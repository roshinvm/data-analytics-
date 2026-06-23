students=[]
def calc_avg(scores):
    if len(scores)==0:
        return 0
    else:
        return sum(scores)/len(scores)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >=80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def add_student ():
    name=input("Enter Student Name: ")
    scores=[]
    while True:
        score_input= input("Enter score (or 'done'): ")
        if score_input.lower()== "done":
            break
        try:
            score=float(score_input)
            if 0<=score <=100:
                scores.append(score)
            else:
                print("Scores must be in between 0 and 100 ")
        except ValueError:
            print("Invalid input. Enter a number or 'done'.")

    average=calc_avg(scores)
    grade=get_grade(average)

    student={
        "Name":name,
        "Scores":scores,
        "Average":average,
        "Grade":grade
    }
    students.append(student)

    print(f"\n Added {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}\n")

def view():
    if len(students)==0:
        print("\n No Students Found \n")
        return
    print("\n ----Students List----")
    for student in students:
        print(
            f"Name: {student['Name']} |"
            f"Average: {student['Average']} |"
            f"Grade: {student['Grade']}"
        )
    print()

def show():
    if len(students) == 0:
        print("\n No student data found.\n")
        return
    highest = students[0]
    lowest = students[0]
    total_average = 0
    for student in students:
        total_average+=student["Average"]

        if student["Average"] > highest["Average"] :
            highest = student 
        if student["Average"] <lowest["Average"] :
            lowest = student
    class_average= total_average/len(students)

    print("\n--- Class Report ---")
    print(f"Total students: {len(students)}")
    print(
        f"Highest Average: {highest["Name"]}"
        f"({highest["Average"]:.2f})"
    )
    print(
        f"Lowest Average: {lowest["Name"]}"
        f"({lowest["Average"]:.2f})"
    )
    print(f"Class average: {class_average:.2f}\n")

def main():
    while True:
        print("\n=== Grade Calculator ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Class Report")
        print("4. Exit")

        choice=input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice =="2":
            view()
        elif choice == "3":
            show()
        elif choice=="4":
            print("Exiting Program....")
            break
        else:
            print("Invalid Choice. Try again\n")

main()
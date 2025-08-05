def calculate_grades_summary():
    """
    Calculates and summarizes student marks and grades.
    """
    students_data = {}
    while True:
        student_name = input("Enter student name (or 'done' to finish): ")
        if student_name.lower() == 'done':
            break

        marks = []
        for i in range(3):
            while True:
                try:
                    mark = float(input(f"Enter marks for subject {i+1}: "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Invalid marks. Please enter a number between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        students_data[student_name] = marks

    if not students_data:
        print("No student data entered.")
        return

    # Calculate and display summary for each student
    print("\n--- Student-wise Summary ---")
    all_averages = []
    for name, marks in students_data.items():
        total_marks = sum(marks)
        average_marks = total_marks / len(marks)
        all_averages.append(average_marks)

        grade = ""
        if average_marks >= 90:
            grade = "A"
        elif average_marks >= 80:
            grade = "B"
        elif average_marks >= 70:
            grade = "C"
        elif average_marks >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"\nStudent: {name}")
        print(f"  Total Marks: {total_marks}")
        print(f"  Average Marks: {average_marks:.2f}")
        print(f"  Grade: {grade}")

    # Calculate and display class summary
    print("\n--- Class Summary ---")
    if all_averages:
        class_average = sum(all_averages) / len(all_averages)
        print(f"Class Average: {class_average:.2f}")

        topper_name = ""
        max_average = -1
        for name, marks in students_data.items():
            average_marks = sum(marks) / len(marks)
            if average_marks > max_average:
                max_average = average_marks
                topper_name = name

        print(f"Class Topper: {topper_name} with an average of {max_average:.2f}")

if __name__ == "__main__":
    calculate_grades_summary()
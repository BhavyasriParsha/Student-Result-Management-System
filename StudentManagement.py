import os

FILENAME = "student_records.txt"


def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'


def register_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    student_class = input("Enter class: ")
    subject1 = float(input("Enter marks for Subject 1: "))
    subject2 = float(input("Enter marks for Subject 2: "))
    subject3 = float(input("Enter marks for Subject 3: "))

    total = subject1 + subject2 + subject3
    percentage = total / 3
    grade = calculate_grade(percentage)

    with open(FILENAME, "a") as f:
        f.write(f"{name},{roll},{student_class},{subject1},{subject2},{subject3},{total},{percentage:.2f},{grade}\n")
    print("✔ Student registered successfully!")


def view_all_records():
    if not os.path.exists(FILENAME):
        print("❌ No records found.")
        return
    with open(FILENAME, "r") as f:
        for line in f:
            display_student_record(line.strip().split(","))


def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[1] == roll:
                display_student_record(data)
                found = True
                break
    if not found:
        print("❌ Student not found.")


def update_student():
    roll = input("Enter roll number to update: ")
    updated_lines = []
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[1] == roll:
                print("🎯 Existing Record:")
                display_student_record(data)

                print("🔁 Enter new details:")
                data[0] = input("Enter new name: ")
                data[2] = input("Enter new class: ")
                data[3] = float(input("Enter marks for Subject 1: "))
                data[4] = float(input("Enter marks for Subject 2: "))
                data[5] = float(input("Enter marks for Subject 3: "))
                data[6] = float(data[3]) + float(data[4]) + float(data[5])
                data[7] = data[6] / 3
                data[8] = calculate_grade(data[7])
                updated_lines.append(",".join(map(str, data)) + "\n")
                found = True
            else:
                updated_lines.append(line)

    if found:
        with open(FILENAME, "w") as f:
            f.writelines(updated_lines)
        print("✔ Student record updated.")
    else:
        print("❌ Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")
    lines = []
    found = False
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[1] != roll:
                lines.append(line)
            else:
                found = True
    if found:
        with open(FILENAME, "w") as f:
            f.writelines(lines)
        print("🗑 Record deleted.")
    else:
        print("❌ Student not found.")


def display_student_record(data):
    print("\n📄 Student Record")
    print(f"Name       : {data[0]}")
    print(f"Roll No.   : {data[1]}")
    print(f"Class      : {data[2]}")
    print(f"Subject 1  : {data[3]}")
    print(f"Subject 2  : {data[4]}")
    print(f"Subject 3  : {data[5]}")
    print(f"Total      : {data[6]}")
    print(f"Percentage : {data[7]}%")
    print(f"Grade      : {data[8]}\n")


def menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Register Student")
        print("2. View All Records")
        print("3. Search Student")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            register_student()
        elif choice == '2':
            view_all_records()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

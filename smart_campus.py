import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []

def register_student():
    usn = input("Enter USN: ")
    name = input("Enter Student Name: ")

    s1 = int(input("Enter Subject 1 Marks: "))
    s2 = int(input("Enter Subject 2 Marks: "))
    s3 = int(input("Enter Subject 3 Marks: "))

    average = (s1 + s2 + s3) / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    student_courses = []

    print("\nEnter Courses for the Student")
    while True:
        course = input("Enter Course Name (or 'done' to finish): ")
        if course.lower() == "done":
            break
        student_courses.append(course)

    student = {
        "usn": usn,
        "name": name,
        "subject1": s1,
        "subject2": s2,
        "subject3": s3,
        "average": average,
        "grade": grade,
        "courses": student_courses
    }

    students.append(student)

    print("\nStudent Registered Successfully!")
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


def display_records():
    if len(students) == 0:
        print("No Student Records Found")
        return

    print("\n===== STUDENT RECORDS =====")

    for s in students:
        print("\nUSN:", s["usn"])
        print("Name:", s["name"])
        print("Subject 1:", s["subject1"])
        print("Subject 2:", s["subject2"])
        print("Subject 3:", s["subject3"])
        print("Average:", round(s["average"], 2))
        print("Grade:", s["grade"])

        print("Courses Enrolled:")
        if len(s["courses"]) == 0:
            print("  No Courses Enrolled")
        else:
            for course in s["courses"]:
                print("  -", course)

        print("-" * 40)


def search_sort():
    if len(students) == 0:
        print("No Student Data Available")
        return

    sorted_students = sorted(students, key=lambda x: x["average"])

    print("\n===== STUDENTS SORTED BY AVERAGE =====")
    for s in sorted_students:
        print(f"{s['usn']} - {s['name']} - {round(s['average'],2)}")

    search_usn = input("\nEnter USN to Search: ")

    found = False
    for s in students:
        if s["usn"] == search_usn:
            print("\nStudent Found!")
            print("USN:", s["usn"])
            print("Name:", s["name"])
            print("Subject 1:", s["subject1"])
            print("Subject 2:", s["subject2"])
            print("Subject 3:", s["subject3"])
            print("Average:", round(s["average"], 2))
            print("Grade:", s["grade"])
            print("Courses Enrolled:")
            for course in s["courses"]:
                print("  -", course)
            found = True
            break

    if not found:
        print("Student Not Found")


def calculate_fee():
    tuition_fee = 50000
    hostel_fee = int(input("Enter Hostel Fee: "))
    transport_fee = int(input("Enter Transport Fee: "))

    total_fee = tuition_fee + hostel_fee + transport_fee

    print("\n===== FEE DETAILS =====")
    print("Tuition Fee:", tuition_fee)
    print("Hostel Fee:", hostel_fee)
    print("Transport Fee:", transport_fee)
    print("Total Fee:", total_fee)


def save_records():
    with open("student_records.txt", "w") as file:
        file.write("USN,Name,Subject1,Subject2,Subject3,Average,Grade,Courses\n")

        for s in students:
            courses_str = ";".join(s["courses"])

            file.write(
                f"{s['usn']},{s['name']},{s['subject1']},{s['subject2']},"
                f"{s['subject3']},{round(s['average'],2)},{s['grade']},"
                f"{courses_str}\n"
            )

    print("Records Saved Successfully!")


class MissingDirectoryError(Exception):
    pass


def scan_directory():
    path = input("Enter Directory Path: ")

    try:
        if not os.path.exists(path):
            raise MissingDirectoryError("Directory does not exist!")

        print("\n===== DIRECTORY STRUCTURE =====")

        for root, dirs, files in os.walk(path):
            print(root)
            for file in files:
                print("   ", file)

    except MissingDirectoryError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)


def performance_analysis():
    if len(students) == 0:
        print("No Data Available")
        return

    data = []

    for s in students:
        data.append([
            s["usn"],
            s["name"],
            s["subject1"],
            s["subject2"],
            s["subject3"],
            s["average"]
        ])

    df = pd.DataFrame(
        data,
        columns=["USN", "Name", "Subject1", "Subject2", "Subject3", "Average"]
    )

    print("\n===== PERFORMANCE DATA =====")
    print(df)

    print("\n===== PANDAS STATISTICAL SUMMARY =====")
    print(df.describe())

    scores = df[["Subject1", "Subject2", "Subject3"]].to_numpy()

    print("\n===== NUMPY ANALYSIS =====")
    print("Mean Scores:", np.mean(scores, axis=0))
    print("Median Scores:", np.median(scores, axis=0))
    print("Standard Deviation:", np.std(scores, axis=0))

    highest = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    print("\nTop Performer:", highest["Name"], "-", round(highest["Average"], 2))
    print("Lowest Performer:", lowest["Name"], "-", round(lowest["Average"], 2))

    plt.bar(df["Name"], df["Average"])
    plt.title("Student Performance Analysis")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.show()

    df.plot(x="Name", y=["Subject1", "Subject2", "Subject3"], kind="bar")
    plt.title("Subject Wise Comparison")
    plt.ylabel("Marks")
    plt.show()


while True:
    print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
    print("1. Register Student")
    print("2. Display Records")
    print("3. Search and Sort")
    print("4. Fee Calculation")
    print("5. Save Records to File")
    print("6. Directory Scanning")
    print("7. Performance Analysis")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        display_records()
    elif choice == "3":
        search_sort()
    elif choice == "4":
        calculate_fee()
    elif choice == "5":
        save_records()
    elif choice == "6":
        scan_directory()
    elif choice == "7":
        performance_analysis()
    elif choice == "8":
        print("Thank You for Using Smart Campus Information System!")
        break
    else:
        print("Invalid Choice! Please Try Again.")

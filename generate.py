import csv
import random

def generate_grades():
    # Define the number of students and the range of possible grades
    num_students = 50

    # Generate random data for the CSV
    data = []
    for student_id in range(1, num_students + 1):
        student_name = f"Student {student_id}"
        grade = random_int = random.randint(50, 100)
        data.append([student_id, student_name, grade])

    # Define the CSV file path
    csv_file_path = "class_grades.csv"

    # Write the data to the CSV file
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Student Name", "Grade"])  # Write header row
        writer.writerows(data)  # Write data rows

    print(f"Random class grades have been saved to '{csv_file_path}'.")

if __name__ == "__main__":
    generate_grades()

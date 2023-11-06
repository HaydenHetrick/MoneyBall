import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    stu_id TEXT,
                    stu_last TEXT,
                    stu_first TEXT,
                    teacher_class TEXT,
                    grade_period TEXT,
                    time_in TEXT,
                    time_out TEXT
                )''')


def create_record(stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out):
    cursor.execute("INSERT INTO students (stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out))
    conn.commit()
    print("Student Record created successfully.")

def read_records():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for record in records:
        print(record)

def update_record(id, new_stu_id, new_stu_last, new_stu_first, new_teacher_class, new_grade_period, new_time_in, new_time_out):
    cursor.execute("UPDATE students SET stu_id = ?, stu_last = ?, stu_first = ?, teacher_class = ?, grade_period = ?, time_in = ?, time_out = ? WHERE id = ?",
                   (new_stu_id, new_stu_last, new_stu_first, new_teacher_class, new_grade_period, new_time_in, new_time_out, id))
    conn.commit()
    print("Student Record updated successfully.")

def delete_record(id):
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print("Student Record deleted successfully.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create a student record")
        print("2. View all current student records")
        print("3. Update a current student record")
        print("4. Delete a current student record")
        print("5. Exit MoneyBall")

        choice = input("Enter your choice: ")

        if choice == "1":
            stu_id = input("Enter student ID Number: ")
            stu_last = input("Enter last name: ")
            stu_first = input("Enter first name: ")
            teacher_class = input("Enter teacher: ")
            grade_period = input("Enter grade: ")
            time_in = input("Enter time in: ")
            time_out = input("Enter time out: ")
            create_record(stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out)

        elif choice == "2":
            read_records()

        elif choice == "3":
            id = int(input("Enter the ID of the record to update: "))
            new_stu_id = input("Enter new student ID Number: ")
            new_stu_last = input("Enter new last name: ")
            new_stu_first = input("Enter new first name: ")
            new_teacher_class = input("Enter new teacher/class: ")
            new_grade_period = input("Enter new grade/period: ")
            new_time_in = input("Enter new time in: ")
            new_time_out = input("Enter new time out: ")
            update_record(id, new_stu_id, new_stu_last, new_stu_first, new_teacher_class, new_grade_period, new_time_in, new_time_out)

        elif choice == "4":
            id = int(input("Enter the ID of the record to permanently delete: "))
            delete_record(id)

        elif choice == "5":
            print("Exiting MoneyBall.")
            break

        else:
            print("Invalid choice.")

conn.close()

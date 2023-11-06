import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
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
    # Insert a new student record into the database
    cursor.execute("INSERT INTO students (stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out))
    conn.commit()
    print("Record created successfully.")

def read_records():
    # Retrieve and display all student records from the database
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for record in records:
        print(record)

def update_record(id, new_stu_id, new_stu_last, new_stu_first, new_teacher_class, new_grade_period, new_time_in, new_time_out):
    # Update an existing student record
    cursor.execute("UPDATE students SET stu_id = ?, stu_last = ?, stu_first = ?, teacher_class = ?, grade_period = ?, time_in = ?, time_out = ? WHERE id = ?",
                   (new_stu_id, new_stu_last, new_stu_first, new_teacher_class, new_grade_period, new_time_in, new_time_out, id))
    conn.commit()
    print("Record updated successfully.")

def delete_record(id):
    # Delete a student record from the database
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print("Record deleted successfully.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create a new student record")
        print("2. View all student records")
        print("3. Update a student record")
        print("4. Delete a student record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stu_id = input("Enter student ID: ")
            stu_last = input("Enter last name: ")
            stu_first = input("Enter first name: ")
            teacher_class = input("Enter teacher/class: ")
            grade_period = input("Enter grade/period: ")
            time_in = input("Enter time in: ")
            time_out = input("Enter time out: ")
            create_record(stu_id, stu_last, stu_first, teacher_class, grade_period, time_in, time_out)

        elif choice == "2":
            read_records()

        elif choice == "3":
            id = int(input("Enter the ID of the record to update: "))
            new_stu_id = input("Enter new student ID: ")
            new_stu_last = input("Enter new last name: ")
            new_stu_first = input("Enter new first name: ")
            new_teacher_class = input("Enter new teacher/class: ")
            new_grade_period = input("Enter new grade/period: ")
            new_time_in = input("Enter new time in: ")
            new_time_out = input("Enter new time out: ")
            update_record(id, new_stu_id, new_stu_last, new_stu_first, new_teacher_class, new_grade_period, new_time_in, new_time_out)

        elif choice == "4":
            id = int(input("Enter the ID of the record to delete: "))
            delete_record(id)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Close the database connection when done
conn.close()

import sqlite3

password = "admin"
username = "admin"

class main_database:
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    def commit(self):
        self.connection.commit()

    def __init__(self):
        table = "CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,firstname TEXT,lastname TEXT,age INTEGER)"
        self.cursor.execute(table)
        self.commit()

    def add_student(self,id, firstname, lastname, age):
        try:
            add_data_sql = "INSERT INTO student(id,firstname, lastname, age) VALUES (?,?,?,?)"
            self.cursor.execute(add_data_sql, (id,firstname, lastname, set_age(age)))
            self.commit()

        except sqlite3.IntegrityError:
            print("Error: Duplicate ID. Same Index Number Entered\n")

        except Exception as e:
            print(f"Error: {e}")
            print("An unexpected error occurred\n")

    def delete_student(self,id):
        try:
            delete_data_sql = "DELETE FROM student WHERE id=?"
            self.cursor.execute(delete_data_sql, (id,))
            self.commit()
            print("Student has been deleted\n")
        except sqlite3.IntegrityError:
            print("Error: Index Missmatch.\n")

    def delete_all_student(self):
        delete_data_sql = "DELETE FROM student"
        self.cursor.execute(delete_data_sql)
        self.commit()
        print("all data has been deleted")

    def get_students(self):
        select_sql = "SELECT * FROM student"
        self.cursor.execute(select_sql)
        data = self.cursor.fetchall()
        print("\nIndex |"+"\t"+"First Name"+"\t"+"Last Name |"+"\t"+"Age")
        for row in data:
            print("{0} \t {1} \t{2} \t{3}".format(row[0], row[1], row[2], row[3]))

def input_data(data_name):
    value = input(data_name)
    return value
def add_student_details():
    student.add_student(int(input_data("Index : ")), input_data("First Name :"), input_data("Last Name :"), input_data("Age : "))

def validation(username_input, pwd):
    error  = ""
    if username_input == username and pwd == password:
       return True
    else:
        if username_input == username:
            if pwd != password:
                error = "Wrong password"
        elif pwd == password:
            if username_input != username:
                error = "Wrong password"
        else:
            error = "Wrong password or username"
        print("Error : ", error)
        return False


def delete_student_details():
    username_input = input_data("User Name: ")
    pwd = input_data("password: ")

    if validation(username_input, pwd):
        select_id = int(input_data("Select Student ID: "))
        student.delete_student(select_id)

def delete_all_student_details():
    username_input = input_data("User Name: ")
    pwd = input_data("password: ")

    if validation(username_input, pwd):
        student.delete_all_student()

def edit_student_details():
    username_input = input_data("User Name: ")
    pwd = input_data("Password: ")

    if validation(username_input, pwd):
        try:
            select_id = int(input_data("Select Student ID to edit: "))
            existing_data_sql = "SELECT * FROM student WHERE id=?"
            student.cursor.execute(existing_data_sql, (select_id,))
            existing_data = student.cursor.fetchone()

            if existing_data:
                print("\nExisting Details:")
                print("ID:", existing_data[0])
                print("First Name:", existing_data[1])
                print("Last Name:", existing_data[2])
                print("Age:", existing_data[3])

                new_firstname = input_data("Enter new First Name : ")
                new_lastname = input_data("Enter new Last Name : ")
                new_age = input_data("Enter new Age : ")

                update_data_sql = "UPDATE student SET firstname=?, lastname=?, age=? WHERE id=?"
                student.cursor.execute(update_data_sql,(new_firstname, new_lastname, new_age, select_id))
                student.commit()

                print("Student details updated successfully\n")
            else:
                print(f"No student found with ID {select_id}\n")

        except Exception as e:
            print(f"Error: {e}")
            print("An unexpected error occurred\n")

def set_age(age):
    try:
        if int(age) < 18:
            raise ValueError("Age must be 18 or less\n")
        else:
            return str(age)
    except ValueError as e:
        print(f"Error: {e}")
        return None

while True:
    student = main_database()
    print("-------------------------------------------------------------")
    print("   Show Student Details   [1]        Add Student Details [2] ")
    print("   Delete Student         [3]        Delete All Details  [4] ")
    print("   Update Student Details [5]        Exit                [6] ")
    print("-------------------------------------------------------------\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student.get_students()
    elif choice == 2:
        add_student_details()
    elif choice == 3:
        delete_student_details()
    elif choice == 4:
        delete_all_student_details()
    elif choice == 5:
        edit_student_details()
    elif choice == 6:
        exit(1)
    else:
        print("Invalid Input")
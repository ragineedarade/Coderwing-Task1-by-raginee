import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Raginee@2027",
        database="Employedb"
    )


def add_employee(name, age, position, salary):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO Employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)
    cursor.execute(query, values)
    db.commit()
    print(f"Employee {name} added successfully.")
    cursor.close()
    db.close()


def promote_employee(emp_id, new_position=None, new_salary=None):
    db = connect_db()
    cursor = db.cursor()
    if new_position:
        query = "UPDATE Employees SET position = %s WHERE id = %s"
        values = (new_position, emp_id)
        cursor.execute(query, values)
    if new_salary:
        query = "UPDATE Employees SET salary = %s WHERE id = %s"
        values = (new_salary, emp_id)
        cursor.execute(query, values)
    db.commit()
    print(f"Employee with ID {emp_id} promoted successfully.")
    cursor.close()
    db.close()


def display_employees():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM Employees"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Employee Records:")
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":

    add_employee("John Doe", 28, "Developer", 70000)
    add_employee("Jane Smith", 32, "Manager", 85000)

    # Promote an employee
    promote_employee(1, new_position="Senior Developer", new_salary=80000)
    display_employees()

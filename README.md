Employee Management System
This project is a Python-based Employee Management System that interacts with a MySQL database to manage employee records. It allows users to add, remove, promote, and display employees, with all information stored persistently in the MySQL database.

Prerequisites
Python: Make sure you have Python 3 installed on your machine.
MySQL: Install MySQL server (you can use XAMPP, WAMP, or MySQL Workbench).
Python MySQL Connector: Install the mysql-connector-python package to enable Python to connect to the MySQL database.
Setup Instructions
Step 1: Install MySQL and Create the Database
Install MySQL if you haven't already.

You can use XAMPP or MySQL Workbench to set up a local MySQL server.
Create a Database:

Open MySQL Workbench (or your preferred MySQL interface).
Create a database named employedb:
sql
Copy code
CREATE DATABASE employedb;
Create the Employees Table:

With the employedb database selected, create the Employees table:
sql
Copy code
USE employedb;

CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    position VARCHAR(50),
    salary FLOAT
);
Step 2: Install Python and Required Libraries
Install Python 3 if it’s not already installed.
Install mysql-connector-python:
Open a terminal (or Command Prompt) and run:
bash
Copy code
pip install mysql-connector-python
Step 3: Configure the Database Connection in the Python Script
Edit the index.py script (Python file containing the Employee Management System code) with your MySQL database credentials.

Replace "your_username" and "your_password" with your actual MySQL username and password:

python
Copy code
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",        # Replace with your MySQL username
        password="your_password",     # Replace with your MySQL password
        database="employedb"
    )
Step 4: Employee Management System Functions
The index.py script includes functions for:

Adding an employee
Removing an employee
Promoting an employee (updating position or salary)
Displaying all employees
Each function connects to the MySQL database, performs the specified operation, and closes the connection.

Example Code (index.py)
Here's a sample of what index.py should look like:

python
Copy code
import mysql.connector

# Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",        # Update with your MySQL username
        password="your_password",     # Update with your MySQL password
        database="employedb"
    )

# Add an employee
def add_employee(name, age, position, salary):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO Employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    print("Employee added successfully.")

# Remove an employee
def remove_employee(emp_id):
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM Employees WHERE id = %s"
    cursor.execute(sql, (emp_id,))
    db.commit()
    db.close()
    print("Employee removed successfully.")

# Promote an employee (update position or salary)
def promote_employee(emp_id, new_position=None, new_salary=None):
    db = connect_db()
    cursor = db.cursor()
    if new_position:
        cursor.execute("UPDATE Employees SET position = %s WHERE id = %s", (new_position, emp_id))
    if new_salary:
        cursor.execute("UPDATE Employees SET salary = %s WHERE id = %s", (new_salary, emp_id))
    db.commit()
    db.close()
    print("Employee promoted successfully.")

# Display all employees
def display_employees():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Employees")
    rows = cursor.fetchall()
    db.close()
    for row in rows:
        print(row)

# Example usage
if __name__ == "__main__":
    add_employee("John Doe", 28, "Developer", 70000)
    display_employees()
    promote_employee(1, new_position="Senior Developer", new_salary=80000)
    display_employees()
    remove_employee(1)
    display_employees()
Step 5: Run the Script
Open a terminal or command prompt in the directory where index.py is saved.
Run the script:
bash
Copy code
python index.py
Features
Add Employee: Adds a new employee to the Employees table.
Remove Employee: Deletes an existing employee based on the emp_id.
Promote Employee: Updates an employee’s position and/or salary.
Display Employees: Fetches and displays all employee records from the database.
Troubleshooting
If you encounter connection errors, verify the MySQL server is running and that your credentials (username, password) are correct.
Ensure the employedb database and Employees table are correctly set up as shown in Step 1.
Additional Notes
This script can be expanded with a more advanced user interface using frameworks like Tkinter or Flask for web applications.
Remember to keep your database password secure and avoid hardcoding sensitive information in production.

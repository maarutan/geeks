import sqlite3 as sql
import os

if os.path.exists("person.db"):
    os.remove("person.db")

with sql.connect("person.db") as c:
    cursor = c.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS departments (
            departmentId INTEGER PRIMARY KEY,
            departmentName TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO departments (departmentId, departmentName)
        VALUES 
            (101, 'HR'),
            (102, 'IT'),
            (103, 'Sales')
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            employeeId INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            departmentId INTEGER NOT NULL,
            FOREIGN KEY (departmentId) REFERENCES departments(departmentId)
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO employees (firstName, lastName, departmentId)
            VALUES 
                ('marat', 'arzymatov', 101),
                ('kamila', 'azybekova', 101),
                ('sergey', 'petrov', 102),
                ('maria', 'kozlova', 102),
                ('alexander', 'sidorov', 103),
                ('olga', 'alekseeva', 103)
        """
    )
    for row in cursor.execute("SELECT * FROM employees"):
        print(row)

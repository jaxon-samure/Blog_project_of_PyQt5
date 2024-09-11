import mysql.connector
from os import system

system("clear")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1!"
)

kr = db.cursor()

def createDatabase():
    kr.execute("CREATE DATABASE IF NOT EXISTS school;")
    db.commit()

def createTable():
    kr.execute("USE school;")
    
    kr.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(32),
            last_name VARCHAR(64),
            salary DECIMAL(10, 2),
            experience INT,
            branch VARCHAR(50)
        );
    """)

    
    kr.execute("""
        INSERT INTO teachers (first_name, last_name, salary, experience, branch) VALUES
        ('Elmore', 'Jennick', 7.76, 6, 'Norfolk County'),
        ('Brendon', 'Smithend', 3.54, 6, 'Longos'),
        ('Sonny', 'Bonanno', 6.35, 8, 'Bakersfield'),
        ('Harlen', 'Maskrey', 9.81, 7, 'Shapaja'),
        ('Luella', 'Orrock', 3.43, 0, 'Nowy Staw'),
        ('Amble', 'Astill', 6.97, 2, 'Karakol'),
        ('Aaren', 'Clemerson', 3.71, 4, 'Beiwucha'),
        ('Anstice', 'Cowthart', 0.33, 6, 'Tiro');
    """)
    
    kr.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(32),
            last_name VARCHAR(64),
            monthly_payment DECIMAL(10, 2),  
            course_duration VARCHAR(50),  
            branch VARCHAR(50)
        );
    """)
    
    kr.execute("""
        INSERT INTO students (first_name, last_name, monthly_payment, course_duration, branch) VALUES
        ('Korella', 'Attard', 6.84, '11-312-9547', 'Yacimiento Río Turbio'),
        ('Farlie', 'Itzkin', 5.19, '80-822-5805', 'Dashi'),
        ('Grace', 'Rippin', 9.84, '01-209-7140', 'Wlingi'),
        ('Bret', 'Clemont', 3.40, '03-132-4754', 'São Mateus do Maranhão'),
        ('Bethina', 'Fodden', 4.51, '36-094-8591', 'Luoyang'),
        ('Kaitlynn', 'Bernakiewicz', 7.90, '94-740-5097', 'Chervone'),
        ('Karolina', 'Parmer', 4.74, '61-756-4696', 'Praya'),
        ('Reinhard', 'Crocetti', 5.18, '69-576-6666', 'Bobon');
    """)
    
    db.commit()

createDatabase()
createTable()

kr.close()
db.close()
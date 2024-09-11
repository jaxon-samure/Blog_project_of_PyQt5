import mysql.connector
from os import system
system("clear")


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1!",
    database = "testdb"
)

kr = db.cursor()

def createTable():
    
    kr.execute("""
        CREATE TABLE IF NOT EXISTS db_ui (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            dori_name VARCHAR(50),
            price FLOAT 
        );
    """)
    
    
    
def insert(ID: int, dori_nomi: str, price: int):
    kr.execute("""
        INSERT INTO db_ui(ID, dori_name, price) VALUES(%s, %s, %s);       
        """, (ID, dori_nomi, price))
    
    db.commit()
    
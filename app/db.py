import sqlite3
import json
import requests
from datetime import datetime

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('DROP TABLE IF EXISTS PresidentServe;')
    cursor.execute('DROP TABLE IF EXISTS President;')

     # Create President table
    table1 = '''
        CREATE TABLE President (
            presidentID INTEGER PRIMARY KEY AUTOINCREMENT,
            presidentName VARCHAR(100) NOT NULL,
            DOB DATE NOT NULL,
            Death DATE DEFAULT NULL,
            First_Lady VARCHAR(100),
            Score INTEGER DEFAULT NULL
        );
    '''

    # Create PresidentServe table
    table2 = '''
        CREATE TABLE PresidentServe (
            serveID INTEGER PRIMARY KEY,
            presidentID INTEGER NOT NULL,
            VicePresident VARCHAR(100),
            Year INTEGER NOT NULL,
            Description TEXT,
            FOREIGN KEY(presidentID) REFERENCES President(presidentID)
        );
    '''
 
    cursor.execute(table1)
    cursor.execute(table2)

    conn.commit()

    conn.close()

def insert_data_fromJSON():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    url = 'http://127.0.0.1/pres'
    response = requests.get(url)

    # Prepare the insert query
    insert_query = '''
    INSERT INTO President (presidentName, DOB, Death, First_Lady, Score)
    VALUES (?, ?, ?, ?, ?);
    '''

    # insert_query2 = '''
    # INSERT INTO PresidentServe (serveID : year Served, presidentID: check if name equal to another database grabid from that president , VicePresident: Grab, Description: Grab)
    # VALUES (?, ?, ?, ?);
    # '''

    if response.status_code == 200:
        data = response.json()
        for key in data:
            president = data[key]
            birth_death = president["Birth-Death "].split("\u2013")
            if len(birth_death) == 2:
                birth = birth_death[0]
                death = birth_death[1]
                if death == '(living)':
                    death = None
            else:
                 birth = birth_death[0]
                 death = None
            cursor.execute(insert_query, (president["Name"], birth, death, president["First Lady"], None))
    else:
        print("Fail to retrieve data")

    # Commit the transaction to save the changes
    conn.commit()

    # Optionally, print a success message
    print("Data inserted successfully.")

    # Close the connection
    conn.close()

def timeConverter(date):

    if date == None:

        return None

    date = date.strip()

    date_obj = datetime.strptime(date, "%B %d, %Y")

    formatted_date = date_obj.strftime("%Y-%m-%d")

    print(formatted_date)

    return formatted_date

 

def remove_duplicates():

    conn = sqlite3.connect('database.db')  # Replace with your database file name

    cursor = conn.cursor()

 

    cursor.execute('''

    SELECT presidentName, COUNT(*)

    FROM President

    GROUP BY presidentName

    HAVING COUNT(*) > 1;

    ''')

 

    duplicates = cursor.fetchall()

 

    if duplicates:

        print("Duplicates found:")

        for row in duplicates:

            print(f"President Name: {row[0]}, Count: {row[1]}")

 

        cursor.execute('''

        DELETE FROM President

        WHERE presidentID NOT IN (

            SELECT MIN(presidentID)

            FROM President

            GROUP BY presidentName

        );

        ''')

 

        conn.commit()

        print("Duplicates removed successfully.")

 

   

    conn.close()




# create_table()
insert_data_fromJSON()

remove_duplicates()

 

 





 
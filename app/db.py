import sqlite3
import json
import requests
from datetime import datetime

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def create_table():
    try:
        # Enable foreign key constraints
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Drop tables if they exist
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
                Score INTEGER DEFAULT 0, 
                ModifyDate DATE DEFAULT NULL, 
                numVote INTEGER DEFAULT 0, 
                URL VARCHAR(100) DEFAULT NULL
            );
        '''

        # Create PresidentServe table
        table2 = '''
            CREATE TABLE PresidentServe (
                serveID INTEGER PRIMARY KEY AUTOINCREMENT,
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
        print("Tables created successfully.")

    except sqlite3.Error as e:
        print("An error occurred while creating tables:", e)




def insert_data_fromJSON():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    url = 'http://127.0.0.1:81/pres'
    response = requests.get(url)

    # Prepare the insert queries
    insert_president_query = '''
    INSERT INTO President (presidentName, DOB, Death, First_Lady, Score, numVote, URL)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''

    insert_president_serve_query = '''
    INSERT INTO PresidentServe (presidentID, VicePresident, Year, Description)
    VALUES (?, ?, ?, ?);
    '''

    if response.status_code == 200:
        data = response.json()
        for key in sorted(data.keys(), key=int):
            print(key)
            president = data[key]
            
            # Parse Birth and Death dates
            birth_death = president["Birth-Death "].split("\u2013")
            if len(birth_death) == 2:
                birth = birth_death[0].strip()
                death = birth_death[1].strip()
                if death == '(living)':
                    death = None
            else:
                birth = birth_death[0].strip()
                death = None
            
            # Insert into President table
            cursor.execute(
                insert_president_query, 
                (president["Name"], birth, death, president["First Lady"], None, 0, president["IMG filepath"])  # Default score and numVote
            )
            
            # Get the last inserted presidentID
            president_id = cursor.lastrowid
            
            # Insert into PresidentServe table
            if "Years Served" in president and "Vice President" in president:
                years = president["Years Served"].split(",")  # Assuming years are comma-separated
                vice_president = president["Vice President"]
                description = president.get("Description", None)  # Optional key
                
                for year in years:
                    year = year.strip()
                    cursor.execute(
                        insert_president_serve_query, 
                        (president_id, vice_president, int(year), description)
                    )
    else:
        print("Failed to retrieve data from the API.")

    # Commit the transaction to save the changes
    conn.commit()

    # Optionally, print a success message
    print("Data inserted successfully into President and PresidentServe tables.")

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
# insert_data_fromJSON()

# remove_duplicates()

 

 





 
import sqlite3

conn = sqlite3.connect('user_comp.db')

def create_users_table(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            active INTEGER NOT NULL,
            date_created DATE NOT NULL,
            hire_date DATE,
            user_type TEXT
        );
        """
    )

def create_assessments_table(conn):
    conn.execute(
    '''
    CREATE TABLE Assessments (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        name         TEXT    DEFAULT (0),
        date_created TEXT
    );
    '''
    )
    
def create_competencies_table(conn):
    conn.execute('''
    CREATE TABLE Competencies (
        user_id       INTEGER PRIMARY KEY
                          REFERENCES Users (id),
        assessment_id INTEGER REFERENCES Competencies (assessment_id),
        score         INTEGER,
        date_taken    TEXT,
        manager_id    INTEGER REFERENCES Users (id) 
    );
    '''
    )
def insert_users_data(conn):
    conn.execute(
        """
        INSERT INTO Users (first_name, last_name, phone, email, password, active, date_created, hire_date, user_type)
        VALUES
            ('Peter', 'Parker', '555-1234', 'spiderman@example.com', 'password123', 1, '2023-04-09', '2022-01-01', 'Manager'),
            ('Clark', 'Kent', '555-5678', 'superman@example.com', 'password123', 1, '2023-04-09', '2022-01-02', 'Employee'),
            ('Bruce', 'Wayne', '555-2468', 'batman@example.com', 'password123', 1, '2023-04-09', '2022-01-03', 'Employee'),
            ('Diana', 'Prince', '555-3698', 'wonderwoman@example.com', 'password123', 1, '2023-04-09', '2022-01-04', 'Employee'),
            ('Arthur', 'Curry', '555-1357', 'aquaman@example.com', 'password123', 1, '2023-04-09', '2022-01-05', 'Employee'),
            ('Barry', 'Allen', '555-2468', 'theflash@example.com', 'password123', 1, '2023-04-09', '2022-01-06', 'Employee'),
            ('Hal', 'Jordan', '555-6789', 'greenlantern@example.com', 'password123', 1, '2023-04-09', '2022-01-07', 'Employee'),
            ('Ray', 'Palmer', '555-2345', 'atom@example.com', 'password123', 1, '2023-04-09', '2022-01-08', 'Employee'),
            ('Oliver', 'Queen', '555-7890', 'greenarrow@example.com', 'password123', 1, '2023-04-09', '2022-01-09', 'Employee'),
            ('Billy', 'Batson', '555-3579', 'shazam@example.com', 'password123', 1, '2023-04-09', '2022-01-10', 'Employee')
        """
    )
    conn.commit()

def select_all_(conn):
    cursor = conn.execute('SELECT id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active FROM Users')
    return cursor.fetchall()

def select_user_by_id(conn, user_id):
    cursor = conn.execute('SELECT id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active FROM Users WHERE id = ?', (user_id,))
    return cursor.fetchone()

def select_user_by_name(conn, first_name):
    fields = ('User_ID', 'First Name', 'Last Name', 'Phone', 'Email', 'Password', 'Date Created', 'Date Hired', 'User Class', 'Status')
    like_name = "%" + first_name + "%"
    result = conn.execute(sql_select_user_by_name, (like_name,))
    data = result.fetchall()
    print(f'{fields[0]:>4} {fields[1]:<30} {fields[2]:<15}   {fields[3]:>7}   {fields[4]:<13} {fields[5]:<45}')
    for row in data:
        print(f'{row[0]:>4} {row[1]:<30} {row[2]:<15}   {row[3]:>7}   {row[4]:<13} {row[5]:<45}')
    return data

sql_select_all = '''
SELECT id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active
FROM Users
'''

sql_select_user_by_id = '''
SELECT id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active
FROM Users
WHERE id = ? 
'''

sql_select_user_by_name = '''
SELECT id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active
FROM Users
WHERE LOWER(first_name) LIKE ?
'''

sql_add_new_user = '''
INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type, active) values(?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

sql_update_user = '''
UPDATE Users
SET first_name = ?, last_name = ?, phone = ?, email = ?, password = ?, date_created = ?, hire_date = ?, user_type = ?, active = ?
WHERE id = ?
'''
sql_delete_user = '''
DELETE 
FROM Users
Where id = ?
'''
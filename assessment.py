import sqlite3

from datetime import date

today = date.today()

class Assessment:
    def __init__(self, name=0, date_created=today, id=None):
        self.id = id
        self.name = name
        self.date_created = date_created
        
    def update_name(self, new_name):
        self.name = new_name
        
    def __str__(self):
        return f"Assessment Name: {self.name}, Date Created: {self.date_created}"

    @staticmethod
    def add_assessment(name, date_created=today):
        conn = sqlite3.connect('user_comp.db')
        c = conn.cursor()

        c.execute('INSERT INTO Assessments (name, date_created) VALUES (?, ?)', (name, date_created))
        conn.commit()
        conn.close()

        print(f"Assessment '{name}' added to the database with date '{date_created}'")
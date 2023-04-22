import sqlite3
from datetime import datetime

class Competency:
    def __init__(self, user_id, assessment_id, score, date_taken, manager_id):
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.score = score
        self.date_taken = date_taken
        self.manager_id = manager_id
        
    def __str__(self):
        return f"User ID: {self.user_id}, Assessment ID: {self.assessment_id}, Score: {self.score}, Date Taken: {self.date_taken}, Manager ID: {self.manager_id}"

    @staticmethod
    def create_competency(user_id, assessment_id, score, date_taken, manager_id):
        new_competency = Competency(user_id, assessment_id, score, date_taken, manager_id)

        conn = sqlite3.connect('user_comp.db')
        c = conn.cursor()

        date_taken_obj = datetime.strptime(date_taken, '%Y-%m-%d')

        c.execute('INSERT INTO Competencies (user_id, assessment_id, score, date_taken, manager_id) VALUES (?, ?, ?, ?, ?)',
                  (new_competency.user_id, new_competency.assessment_id, new_competency.score, date_taken_obj, new_competency.manager_id))

        conn.commit()

        conn.close()

        return new_competency

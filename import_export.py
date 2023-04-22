import csv
import sqlite3

class input_output:
    def __init__(self, user_comp):
        self.user_comp = user_comp

    def export_data_to_csv(self, Competencies, output):
        conn = sqlite3.connect(self.user_comp)
        cur = conn.cursor()
        cur.execute('SELECT * FROM {}'.format(Competencies))
        col_names = [description[0] for description in cur.description]

        with open(output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(col_names)
            for row in cur.fetchall():
                writer.writerow(row)

        conn.close()

    def import_data_from_csv(self, Assessment_Results, input):
        with open(input, 'r') as csvfile:
            reader = csv.reader(csvfile)
            conn = sqlite3.connect(self.user_comp)
            cur = conn.cursor()
            for row in reader:
                cur.execute('INSERT INTO {} VALUES ({})'.format(Assessment_Results, ','.join(['?' for _ in row])), row)

            conn.commit()
            conn.close()

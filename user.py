import sqlite3
from datetime import datetime
import bcrypt


class User:
    def __init__(
        self,
        first_name,
        last_name,
        phone,
        email,
        password,
        active=1,
        date_created=None,
        hire_date=None,
        user_type="User",
        id=None,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = self.hash_password(password)
        self.active = active
        self.date_created = date_created or datetime.now().date()
        self.hire_date = hire_date
        self.user_type = user_type

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nActive: {self.active}\nUser Type: {self.user_type}"

    def save(self):
        conn = sqlite3.connect("user_comp.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT OR REPLACE INTO Users (id, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type) \
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                self.id,
                self.first_name,
                self.last_name,
                self.phone,
                self.email,
                self.password,
                self.active,
                self.date_created,
                self.hire_date,
                self.user_type,
            ),
        )

        conn.commit()
        conn.close()

    def display_user_table(self):
        print(
            f"{self.id:<5} {self.first_name:<15} {self.last_name:<15} {self.phone:<15} {self.email:<30} {self.active:<8} {self.user_type:<10}"
        )

    @staticmethod
    def display_user_table_header():
        print(
            f'{"ID":<5} {"First Name":<15} {"Last Name":<15} {"Phone":<15} {"Email":<30} {"Active":<8} {"User Type":<10}'
        )

    @staticmethod
    def get_user_by_name(name):
        conn = sqlite3.connect("user_comp.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT first_name, last_name, phone, email, password, active, date_created, hire_date, user_type, id FROM Users WHERE first_name LIKE ? OR last_name LIKE ?",
            (f"%{name}%", f"%{name}%"),
        )
        rows = cur.fetchall()

        users = []
        for row in rows:
            user = User(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
            )
            users.append(user)

        conn.close()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        conn = sqlite3.connect("user_comp.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT first_name, last_name, phone, email, password, active, date_created, hire_date, user_type, id FROM Users WHERE id=?",
            (user_id,),
        )
        user_data = cur.fetchone()

        conn.close()

        if user_data:
            user = User(*user_data)
            return user

        return None

    @staticmethod
    def get_all_users():
        conn = sqlite3.connect("user_comp.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT first_name, last_name, phone, email, password, active, date_created, hire_date, user_type, id FROM Users"
        )
        rows = cur.fetchall()

        users = []
        for row in rows:
            user = User(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
            )
            users.append(user)

        conn.close()
        return users

    @staticmethod
    def display_all_users():
        
        all_users = User.get_all_users()

        User.display_user_table_header()

        for my_user in all_users:
            my_user.display_user_table()

    @staticmethod
    def validate_email(email):
        regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if regex.search(email):
            return True
        else:
            return False

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def login(email, password):
        conn = sqlite3.connect("user_comp.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT first_name, last_name, phone, email, password, active, date_created, hire_date, user_type, id FROM Users WHERE email = ?",
            (email,),
        )
        row = cur.fetchone()

        conn.close()

        if row is None:
            return "Invalid Username"  

        user = User(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
        )
        print(user.password)
        
        if bcrypt.checkpw(password, user.password):
            return user
        else:
            return None


    @staticmethod
    def update_passwords():
        conn = sqlite3.connect("user_comp.db")
        cur = conn.cursor()

        cur.execute("SELECT id, password FROM Users")
        rows = cur.fetchall()

        for row in rows:
            user_id = row[0]
            plaintext_password = row[1]
            hashed_password = bcrypt.hashpw(
                plaintext_password.encode("utf-8"), bcrypt.gensalt()
            )
            cur.execute(
                "UPDATE Users SET password = ? WHERE id = ?",
                (hashed_password.decode("utf-8"), user_id),
            )

        conn.commit()
        conn.close()


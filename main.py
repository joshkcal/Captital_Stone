from menu import *
from user import *
from competency import *
from assessment import *
from datetime import date


today = date.today()

while True:
    print("-Login to the Database- ")
    email = input("Enter your email: ")
    password = input("Enter your password: ").encode('utf-8')
    # current_user = User.login(email, password)
    try:
        current_user = User.login(email, password)
        # current_user = User.get_user_by_id(1)
        print(current_user)
        if current_user is not None:
            print("Login successful!")
        if current_user.user_type == "Manager":
            print("You are now operating as a Manager")
            manager_menu_options = ["View", "Edit", "Delete"]
            manager_menu = Menu(manager_menu_options)
            manager_menu.display()
            choice = manager_menu.get_choice()
            if choice == 1:
                users = User.get_all_users()
                User.display_user_table_header()
                for user in users:
                    user.display_user_table()
                    
            elif choice == 2:
                print("menu opt2")
                
            elif choice == 3:
                print("menu opt 3")
                
        elif current_user.user_type == "Employee":
            employee_menu_options = ["View", "Edit"]
            employee_menu = Menu(employee_menu_options)
            employee_menu.display()
            choice = employee_menu.get_choice()
            if choice == 1:
                print(current_user)
                    
            elif choice == 2:
                new_first_name = input(f"Edit first name({current_user.first_name}): ")
                if new_first_name.strip():
                    current_user.first_name = new_first_name
                    
                new_last_name = input(f"Edit last name({current_user.last_name}): ")
                if new_last_name.strip():
                    current_user.last_name = new_last_name
                    
                new_email = input(f"Edit email({current_user.email}): ")
                if new_email.strip():
                    current_user.email = new_email
                    
                new_phone = input(f"Edit Phone number({current_user.phone}): ")
                if new_phone.strip():
                    current_user.phone = new_phone
                    
                new_active = input(f"Edit active status({current_user.active}): ")
                if new_active.strip():
                    current_user.active = new_active
                    
                password1 = input("Enter a new password")
                if password1.strip() != '':
                    password2 = input("Please enter the password a second time")
                    if password1 != password2:
                        print("passwords don't match - try again")
                    else:
                        current_user.password = password1
    except ValueError as e:
        print("Error:", e)
        current_user.save()

class Menu:
    def __init__(self, options):
        self.options = options

    def display(self):
        print("Please select an option:")
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice > 0 and choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                

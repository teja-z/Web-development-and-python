class PasswordManager:
    def __init__(self):
        self.old_passwords = []  # List to store all past passwords

    def get_password(self):
        # Returns the current password (the last item in the list)
        if self.old_passwords:
            return self.old_passwords[-1]
        return None  # If no password has been set yet

    def set_password(self, new_password):
        # Checks if the new password is different from all past passwords
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)  # Set the new password
            return True
        else:
            return False  # The new password is the same as an old one

    def is_correct(self, password):
        # Returns True if the provided password matches the current password
        return password == self.get_password()


def main():
    password_manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Set a new password")
        print("2. Get the current password")
        print("3. Check if a password is correct")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            new_password = input("Enter the new password: ")
            if password_manager.set_password(new_password):
                print("Password successfully set!")
            else:
                print("Password cannot be the same as an old one.")
        
        elif choice == "2":
            current_password = password_manager.get_password()
            if current_password:
                print(f"Your current password is: {current_password}")
            else:
                print("No password has been set yet.")
        
        elif choice == "3":
            password_to_check = input("Enter the password to check: ")
            if password_manager.is_correct(password_to_check):
                print("The password is correct.")
            else:
                print("The password is incorrect.")
        
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

import string
import secrets

# Global Variables
employee_list = []
employee_passwords = {}  # Dictionary to store Employee IDs and passwords.

# Function Definitions
def employee_name():
    while True:
        name = input("Enter your full name: ")

        if any (char.isdigit()for char in name):
            print("Name cannot contain any numerical values. ")
        else:
            return name
        
def employee_id_number():
    while True:

        employee_id_number = input("Enter your ID number: ")

        if not employee_id_number.isdigit():
            print("ID number can only be numerical values, therefore cannot contain alphabets or special characters")
        
        elif len(employee_id_number) > 13:
            print("ID number exceeds limit. \n Please try again ")
        
        elif len(employee_id_number) < 13:
            print("Your ID number may be missing a few digits. \n Please check and try again. ")

        else:
            return employee_id_number


def generate_employee_id(name, id_no):
    employee_id = f"{name[:3].upper()}{id_no[4:8]}"
    return employee_id


def existing_employee(employee_id):

    if employee_id not in employee_list:
        print("This is not a valid Employee ID. Double-check and try again.")

        return False

    return True

def generate_password(length=12):

    alphabet = string.ascii_letters + string.digits

    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return password



def forgot_password(employee_id):

    if employee_id not in employee_passwords:
        print("Invalid Employee ID. Please check and try again.")

        return

    print(f"Password reset requested for Employee ID: {employee_id}")

    temp_password = generate_password(8)

    employee_passwords[employee_id] = temp_password

    print(f"Your temporary password is: {temp_password}. Please log in and reset your password. Okay?")

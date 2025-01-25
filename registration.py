import string
import secrets
#Here we register the company employees, and generate their Employee IDs.
#Store the generated Ids in a list to be accesed later.
#generate a password the employee will use to access their account later

employee_list = []

def employee_name():
    return input ("Enter your name:  ")

def employee_id_number():
    while True:
        employee_id_number = input("Enter your ID number: ")
        if len(employee_id_number)> 13:
            print("Exceeds maximum number of digits. ")
        elif len(employee_id_number)< 13:
            print("ID number seems to be missing a few digits please double check and try again. ")

        else:
            return employee_id_number

def generate_employee_id(name, id_no):
    employee_id = f"{name [:3].upper()}{id_no[4:8]}"
    return employee_id


def existing_employee(employee_id , employee_list):
    if employee_id not in employee_list:
        print("This is not a valid Employee ID, double check and try again.")
    else:
        return True


        
def generate_password(length = 12):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet)for _ in range(length))

    return password

    


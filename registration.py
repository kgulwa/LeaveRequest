#Here we register the company employees, and generate their Employee IDs.
#Store the generated Ids in a list to be accesed later.

def employee_name():
    employee_name = input("Enter your name: ")
    return employee_name

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


def existing_employee_id(employee_id):
    while True:
        existing_employee_id = []
        existing_employee_id.append(employee_id)

    if employee_id not in existing_employee_id:
        print("This is not a valid Employee ID. Try Again")
    else:
        return employee_id
        
    


import registration

def login(employee_id, existing_employee_id):
    print("Good Day!")
    while True:
        user_id = input("Enter your valid Employee ID: ")
    if user_id in existing_employee_id: #checking if the user/ employee id entered exists in the list of existing IDs
        print(user_id)
    if user_id not in existing_employee_id:
        print("The ID you have entered does not exist on our system, please double check or register as a new user. ")


def welcome_message(employee_name): # message to be displayed after a succesful login
    print(f"Good Day {employee_name}. What would you like to do today? ")

    

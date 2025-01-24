import registration

def login(employee_id, existing_employee_id):
    print("Good Day!")
    while True:
        user_id = input("Enter your valid Employee ID: ")
    if user_id in existing_employee_id:
        print(user_id)
    

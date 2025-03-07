import registration
import login

def main():
    print("Good Day!! Welcome to Employee Management System.")
    print("1. Register (New User)")
    print("2. Login (Existing User)")
    
    while True:
        choice = input("Enter your choice (1 to Register, 2 to Login): ").strip()
        
        if choice == "1":
            register()
            break
        elif choice == "2":
            login_user()
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

def register():
    print("\n--- Employee Registration ---")
    
    name = registration.employee_name()
    id_no = registration.employee_id_number()
    department = input("Enter your department: ").strip()

    employee_id = registration.generate_employee_id(name, id_no)
    print(f"\nYour auto-generated Employee ID is {employee_id}")
    print("*Remember this ID for future reference.*")

    password = registration.generate_password(12)
    print(f"Your auto-generated password is: {password}")
    print("*Keep it safe and DO NOT share with anyone.*")

    # Register employee
    registration.register_employee(employee_id, name, department, password)

    # Initialize leave balance
    registration.register_leave_balance(employee_id)

def login_user():
    print("\n--- Employee Login ---")
    employee_id = input("Enter your Employee ID: ").strip()
    
    if login.authenticate_user(employee_id):
        print(f"Welcome, {employee_id}!")
    else:
        print("Invalid Employee ID. Please try again or register.")

if __name__ == "__main__":
    main()

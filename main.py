import registration

def main():
    print("Good Day!! Welcome to Employee Registration.")

    name = registration.employee_name()
    id_no = registration.employee_id_number()
    department = input("Enter your department: ").strip()

    employee_id = registration.generate_employee_id(name, id_no)
    print(f"\nYour auto-generated Employee ID is {employee_id}")
    print("*Remember this ID for future references.*")

    # Generate a random password
    password = registration.generate_password(12)
    print(f"Your auto-generated password is: {password}")
    print("*Keep it safe and DO NOT share with anyone.*")

    # Register the employee in the database
    registration.register_employee(employee_id, name, department)

    # Initialize leave balance in the database
    registration.register_leave_balance(employee_id)

if __name__ == "__main__":
    main()

import registration

def main():
    print("Good Day!! Welcome to Employee Registration.")

    name = registration.employee_name()
    id_no = registration.employee_id_number()

    employee_id = registration.generate_employee_id(name, id_no)
    print(f"Your auto-generated Employee ID is {employee_id}\n*Remember this ID for future references.*")

    # Add employee to the system
    registration.employee_list.append(employee_id)

    # Generate and store password
    password = registration.generate_password(12)
    registration.employee_passwords[employee_id] = password

    print(f"Your auto-generated password is: {password}\n*Keep it safe and DO NOT share with anyone.*")

    # Initialize leave balance for new employee
    registration.register_leave_balance(employee_id)

if __name__ == "__main__":
    main()

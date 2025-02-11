import registration

# Corrected list of valid leaves
valid_leave = ["Sick Leave", "Family Responsibility Leave", "Maternity Leave", "Paternity Leave", "Annual Leave"]

def leave_application(employee_id, leave_type, days_requested):
    # Check if employee exists
    if employee_id not in registration.employee_leave_balance:
        print("Error: Employee not found. Please register first.")
        return

    # Keep prompting the user until a valid leave type is entered
    while leave_type not in valid_leave:
        print("Error: Invalid leave type. Please choose from the following options:")
        for leave in valid_leave:
            print(f"- {leave}")
        leave_type = input("Enter a valid leave type: ").strip()

    # Check if requested days are valid
    while True:
        if days_requested <= 0:
            print("Error: Number of days must be greater than zero.")
            days_requested = int(input("Enter the number of days again: "))
        else:
            break

    # Ensure the employee has a leave record for this leave type
    if leave_type not in registration.employee_leave_balance[employee_id]:
        print(f"Error: No leave record found for {leave_type}.")
        return

    # Check if employee has enough leave balance
    if registration.employee_leave_balance[employee_id][leave_type] >= days_requested:
        registration.employee_leave_balance[employee_id][leave_type] -= days_requested
        print(f"Leave approved! {employee_id} now has {registration.employee_leave_balance[employee_id][leave_type]} days left for {leave_type}.")
    else:
        print(f"Error: Insufficient leave balance. {employee_id} has only {registration.employee_leave_balance[employee_id][leave_type]} days left.")

def check_leave_balance(employee_id):
    if employee_id not in registration.employee_leave_balance:
        print("Error: Employee not found in the system. Please register first.")
        return

    print(f"\nLeave balance for {employee_id}:")
    for leave_type, days_left in registration.employee_leave_balance[employee_id].items():
        print(f"{leave_type}: {days_left} days remaining.")

if __name__ == "__main__":
    empl_id = input("Enter your Employee ID to apply for leave: ").strip()

    # Keep asking for leave type until a valid one is provided
    leave_type = input("Enter the type of leave you are applying for: ").strip()
    while leave_type not in valid_leave:
        print("Error: Invalid leave type. Please choose from the following options:")
        for leave in valid_leave:
            print(f"- {leave}")
        leave_type = input("Enter a valid leave type: ").strip()

    # Handle empty or invalid number of days
    while True:
        days_input = input("Enter the number of days: ").strip()
        if not days_input.isdigit():
            print("Error: Please enter a valid number.")
        else:
            days = int(days_input)
            if days > 0:
                break
            else:
                print("Error: Number of days must be greater than zero.")

    leave_application(empl_id, leave_type, days)
    check_leave_balance(empl_id)

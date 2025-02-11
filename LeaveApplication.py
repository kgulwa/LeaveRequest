import registration

valid_leave = ["Sick Leave", "Family Responsibility Leave", "Martenity Leave", "Partenity Leave", "Annual Leave"]

def leave_application(employee_id, leave_type, days_requested ):

    if employee_id not in registration.employee_leave_balance:
        print("Employee not found. Please register first")
        return

    if leave_type not in valid_leave:
        print("Invalid leave type. Please double check the valid leave list.")
        return

    if registration.employee_leave_balance[employee_id][leave_type] >= days_requested:
        registration.employee_leave_balance[employee_id][leave_type] -= days_requested
        print(f"Leave approved! {employee_id} haas {registration.employee_leave_balance[employee_id][leave_type]} days left for {leave_type}.")

    else:
        print(f"Insufficient leave balance. {employee_id} has only {registration.employee_leave_balance[employee_id][leave_type]} days left.")

def check_leave_balance(employee_id):
    if employee_id not in registration.employee_leave_balance:
        print("Employee not found in the system. Please register first.")
        return

    print(f"Leave balance for {employee_id}: ")
    for leave_type, days_left in registration.employee_leave_balance[employee_id].items():
        print (f"{leave_type}: {days_left} days remaining.")


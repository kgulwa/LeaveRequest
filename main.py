import registration
employee_list = []

def main():
    print("Good Day!! Welcome to Employee Registration.")
    name = registration.employee_name()
    id_no = registration.employee_id_number()
    employee_id = registration.generate_employee_id(name,id_no)
    print(f"Your auto generated Employee Id is {employee_id}. Make sure to remember this ID for future references. ")
    employee_list.append(employee_id)
    password = registration.generate_password(12)
    print(f"Your auto generated password is: {password}.  Make sure to keep is safe and DO NOT share with anyone")


if __name__ == "__main__": 
    main()
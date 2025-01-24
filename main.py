import registration

def main():
    print("Good Day!! Welcome to Employee Registration.")
    name = registration.employee_name()
    id_no = registration.employee_id_number()
    employee_id = registration.generate_employee_id(name,id_no)
    print(f"Your auto generated Employee Id is {employee_id}. Make sure to remember this ID for future references. ")
    existing_employee_id = registration.existing_employee_id(employee_id)
    #print(existing_employee_id)


if __name__ == "__main__": 
    main()
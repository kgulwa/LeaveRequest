import registration
# This is where employees apply for leave
#I need a list of valid leaves
#Application statuses
#Leave balance tracker


valid_leave = ["Sick Leave", "Family Responsibility Leave","Maternity Leave","Paternity Leave","Annual Leave",] #list of valid requests

request_status = ["Succesful", "Unsuccesful", "Pending"] # list of leave statuses


leave_entitlement = {
    "Annual Leave": 21,
    "Sick Leave" : 30,
    "Maternity Leave" : 120,
    "Family Responsibility Leave": 3,
} # Dictionary for the leave entitlements in days

employee_leave_balance = {}

def leave_application(employee_name,valid_leave,days_requested):

    while True :
        
        leave_request = input("Please enter the Leave you would like to apply for: ")

        if leave_request in valid_leave:
            return leave_request

        else:
            print("Please double check the list of valid Leave Requests and enter a valid request")


    if employee_name not in employee_leave_balance:
        print()


        
if __name__ == "__main__": 
    leave_application()      

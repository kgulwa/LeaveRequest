# This is where employees apply for leave
#I need a list of valid leaves
#Application statuses
#Leave balance tracker


valid_leave = ["Sick Leave", "Family Responsibility Leave","Maternity Leave","Paternity Leave","Annual Leave",]
request_status = ["Succesful", "Unsuccesful", "Pending"]

def leave_application():
    while True :
        
        leave_request = input("Please enter the Leave you would like to apply for: ")

        if leave_request in valid_leave:
            return leave_request

        else:
            print("Please double check the list of valid Leave Requests and enter a valid request")


        
if __name__ == "__main__": 
    leave_application()      

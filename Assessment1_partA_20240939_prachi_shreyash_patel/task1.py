'''task1 for part A (Assignment 2)'''
requisition_number = 10000    # Starting a global variable with value 10000 

# Single Responsibility __ This function only collects staff info and updates the requisition number and it does not do anything else like approvals or reports.
def staff_info():  # Defined a function called staff_info 
    global requisition_number   # Telling Python that we want to use and change the global variable requisition_number
    requisition_number= requisition_number + 1   # Increase requisition_number by 1 each time the function being called


    staff_date = input("Please enter the date: ") #asking the staff to enter the date
    staff_id = input("Please enter Staff ID: ") #asking the staff yo enter the staff ID
    staff_name = input("Please enter Staff Name: ") #askking the staff enter there name 

# Returning all collected details along with the updated requisition_number for next task
    return staff_date, staff_id, staff_name, requisition_number


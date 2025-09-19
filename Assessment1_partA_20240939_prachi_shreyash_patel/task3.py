'''task 3 part (assignment 2)'''
from task2 import requisitions_total # Importing the requisitions_total function from task2.py

def requisitions_approval():   # Defined a function called requisitions_approval
    # Separation of Concerns This function only handles approval logic
    try:
        # Calling the requisitions_total function to get staff details and total price
        staff_date, staff_id, staff_name, req_id, total_price = requisitions_total()

        status = "Pending"          # By default, setting status as "Pending"
        approval_code = "Not available"    # By default, approval code is not available

        # approval rule
        # over here  the total price is less than 500 and mark it as approved
        if total_price < 500:
            status = "Approved"
            # Createdd an approval code by joining staff_id with last 3 digits of requisition number
            approval_code = staff_id + str(req_id)[-3:]
        # Return all details: staff info, requisition ID, total cost, status, and approval code for next task
        return staff_date, staff_id, staff_name, req_id, total_price, status, approval_code

# Error Handling __ Catches wrong input so program doesn’t crash
    except ValueError:   # if user enters wrong input for numbers
        print("Error: please enter valid numbers for item costs.")
        Return default values if there is an error
        return None, None, None, None, 0, "Pending", "Not available"

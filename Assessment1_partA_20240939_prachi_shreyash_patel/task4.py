'''task4 for part A (assignment 2)'''
from task3 import requisitions_approval  # Importing the requisitions_approval function from task3.py

def display_requisitions(): # Defined a function called display_requisitions
    # Starting a loop so we can keep adding requisitions until the user stops

    while True:
        # Calling requisitions_approval to get staff info, requisition ID, cost, status, and approval ref
        staff_date, staff_id, staff_name, req_id, total_price, status, approval_ref = requisitions_approval()

        # Clean Code __ Outputs are simple and user-friendly instead of being too complex
        # only display if staff info was entered correctly
        if staff_date is not None:
            print("\nPrinting Requisitions:")  # New line + heading
            print("Date:", staff_date)  # Shows the entered date
            print("Requisition ID:", req_id)  # Shows the requisition number
            print("Staff ID:", staff_id) # Shows the staff ID
            print("Staff Name:", staff_name) # Shows the staff name
            print("Total: $", total_price)  # Shows the total cost of items
            print("Status:", status)  # Shows whether it's Pending or Approved
            print("Approval Reference Number:", approval_ref) # Shows the approval code

        # ask staff if they want another requisition
        again = input("\nDo you want to add another requisition? (yes/no): ")
        if again.lower() != "yes":   # If the answer is not "yes" (any other input), stop the loop
            break
            break

# run the function when thw program will start 
display_requisitions()

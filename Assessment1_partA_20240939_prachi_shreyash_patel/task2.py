'''task 2 for part A (assignment2)'''
from task1 import staff_info   # Importing the staff_info function from task1.py to use the collected details and requisition number
# D.R.Y __ Instead of writing the same code again to collect staff info, this code reuses the staff_info() function from Task 1. This avoids repetition.
def requisitions_total():  # Defined a function called requisitions_total
    staff_date, staff_id, staff_name, req_id = staff_info()
        # Calling the staff_info function from task 1 to collect all staff details and requisition number
    # The 4 returned values are stored in separate variables  

    total_price = 0  # start with total price = 0 (we will add item prices over here)
    num_items = int(input("How many items are you adding to this requisition? ")) 
        # asking the user how many items they want to add  (also converting input into an integer) 

    for n in range(1, num_items + 1):        # here is the loop that runs from 1 up to the number of items the user entered 
        item_name = input(f"Item {n} name: ")   # asking for the name of each item 
        item_cost = float(input(f"Enter price of {item_name}: $")) #asking the cost of item 
        total_price =total_price + item_cost # Adding the item’s cost to the running total price

    # After the loop is finished then return all the staff details, requisition number, and total cost for the next task
    return staff_date, staff_id, staff_name, req_id, total_price

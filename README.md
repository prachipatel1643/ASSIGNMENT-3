# ASSIGNMENT-3  

 INTRODUCTION:
 
This activity is a small software system for handaling staff reuisitions. This activity is divided into four tasks. Each task builds on the previous one and introduces a different part of the process, starting from collecting staff details, calculating totals, checking approvals, and finally displaying everything to the user. While writing the code, I also applied several software design principles. These principles are very important because they make the code easy to read, reuse, and maintain in the future. Some principles are applied directly in my code, while others are not used because they are not needed for such a small beginner project. In this file, I will explain what I have done in each task, which principle I used, why it was useful, and which principle I did not use.


EXPLAINATION OF CODE :

TASK_1: staff_info

In Task 1, I started with the basic foundation of the project. I created a function called staff_info() that collects staff details like the date, staff ID, and staff name. At the same time, it also updates a requisition number that increases each time the function is called. This makes sure that every requisition has a unique number.

The main principle I used here is Single Responsibility. This function only has one job: to collect staff information and update the requisition number. It does not do anything else like approvals or displaying results. Keeping one function focused on one role makes it easier to test and reuse later.

TASK_2: requisitions_total

In Task 2, I extended the program by adding a way to collect multiple item names and prices. I also calculated the total cost of all items in a requisition. To avoid repeating code, I imported the staff_info() function from Task 1 instead of rewriting it.

The main principle I used here is D.R.Y (Don’t Repeat Yourself). Instead of writing the same code again to collect staff details, I reused the function from Task 1. This makes the code shorter, avoids duplication, and reduces mistakes. If I ever need to update how staff information is collected, I only need to change it in Task 1 and it will automatically update everywhere else.


TASK_3: requisitions_approval

In Task 3, I introduced business logic to check whether a requisition is approved. The rule I used was that if the total price is below $500, the requisition is marked as “Approved” and an approval code is created. If it is more than that, the requisition stays “Pending.”

Here I used Separation of Concerns. The approval function only focuses on checking the total price and creating the approval code. It does not handle staff input or printing results. This makes the function easier to change later, for example, if more approval rules need to be added.

I also added Error Handling as part of a refactor mindset. If the user enters invalid input, like letters instead of numbers for item costs, the program catches the error and shows a message instead of crashing. This improves user experience and makes the program more reliable.


TASK_4:display_requisitions

In Task 4, I completed the system by showing all the collected information in a clear format. The function displays staff details, requisition ID, total price, approval status, and approval code. I also added a loop so that the user can keep adding requisitions until they decide to stop.

Here I applied the principle of Clean Code over Clever Code. The goal was to make the output user-friendly and simple to read. Instead of making the printing logic complicated, I kept it direct and clear so that anyone using the program can easily see the results. This also helps when the program is tested or explained to others.


SOFTWARE DESIGN PRINCIPLES THAT I HAVE NOT USED:

1)K.I.S.S (Keep It Simple, Stupid)

Although some tasks naturally followed simplicity, I didn’t explicitly label it as a principle in the code. The main focus was on functional correctness and applying other explicit principles.

2)Open / Closed Principle

This principle is for making functions extendable without modifying existing code. Since my project is small and beginner-level, I didn’t add multiple rules or extensions that required this principle.

3) Composition > Inheritance

My code does not use classes extensively with inheritance. I only used simple functions, so composition versus inheritance was not needed.

4) Y.A.G.N.I (You Aren’t Gonna Need It)

Y.A.G.N.I is about not adding extra features before they are needed. I focused only on the required features for this assignment, so the principle was inherently followed but not explicitly applied.

5) Refactor, Refactor, Refactor

The code is beginner-level and straightforward. I wrote it cleanly from the start, so extensive refactoring was not needed during this project.

6) Avoid Premature Optimisation

The program is small and runs fast as is. There was no need to optimize performance early, so this principle wasn’t required for these tasks.


Conclusion

Each task in this project demonstrates how software design principles can guide even a simple program. In Task 1, I focused on keeping the function small and simple. In Task 2, I reused code to avoid duplication. In Task 3, I separated responsibilities and made the program safe against errors. Finally, in Task 4, I made sure the output was clean and user-friendly.

Together, these principles show that good design is not only for big systems but also for small projects. They make the program easier to understand, test, and extend in the future. By applying one or two principles at each stage, I was able to build the project step by step while keeping it simple and reliable.

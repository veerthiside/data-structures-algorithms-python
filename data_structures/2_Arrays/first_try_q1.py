# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this.

# 1
expenses = [2200, 2350, 2600, 2130, 2190]
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
feb_minus_jan = expenses[1] - expenses[0]
print(f"In Feb, you spent ${feb_minus_jan} extra compared to Jan.")

# 2
print(f"Expense in first quarter is of ${sum(expenses[:3])}.")

# other methods:
# ii - manual addition
# print(f"Expense in first quarter is of ${expenses[0]+expenses[1]+expenses[2]}.")

# iii - for loop
# first_quarter_expense = 0
# for i in range(3):
#     first_quarter_expense = first_quarter_expense + expenses[i]
# print(f"Expense in first quarter is of ${first_quarter_expense}.")


# 3
seen_2000 = False
for i in range(len(expenses)):  
    if expenses[i] == 2000:
        print(f"You spent $2000 in the month of {month[i]}.")
        seen_2000 = True

if seen_2000 == False:
    print("Nope, you didn't spend $2000 in any month.")

# other method:
# ii - if else with in
# if 2000 in expenses:
#     print("Yes, you spent $2000.")
# else:
#     print("Nope, you didn't spend $2000 in any month.")

# 4    
expenses.append(1980)
print(expenses)

# 5
expenses[3] -= 200
print(expenses)
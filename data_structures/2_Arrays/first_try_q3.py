# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

max_num = int(input("Enter the max number: "))
odd_num = []
for i in range(1, max_num):
    if i%2 == 0:
        continue
    else:
        odd_num.append(i)

print(f"Odd number(s): {odd_num}.")
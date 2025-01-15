#Task 1 ############################
user_name = input("Please enter your name\n>> ") #store their input as user_name
print(f"Hello {user_name}!") #call user_name in this f-string to use their name
#Task 2 ################################
user_age = input("Please enter your age\n>> ") #store their input as user_age
print(int(user_age) + 5)
#the int function fixes the problem explained on the next line
#print(user_age + 5) fails normally because the input function returns a string
#this means the function tries to add a string and a number which isn't possible,
#returning an error
#Task 3 ####################################
age_progression = input("How many years older do you want to be?\n>> ")
print("You will be " + str(int(user_age) + int(age_progression)) + f" in {age_progression} years")
#This is what you described in the instructions
#This doesn't work because concatenating two strings doesn't add up the values inside those strings
#Instead of concatenating strings you should be adding numbers
#Task 4 ###########################################
hours_worked = float(input("Please enter how many hours you've worked this week\n>> "))
pay_per_hour = float(input("Please enter the amount you make per hour (In USD)\n>> $"))
#Task 5 #################################################
print("Your pay this week will be: $" + str(hours_worked * pay_per_hour) +
      "\nYour estimated annual salary is: $" + str(hours_worked * pay_per_hour * 52))
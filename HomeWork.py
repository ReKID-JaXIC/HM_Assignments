pet_type = "cat"
pet_name = "Sock"
print(f"I have a {pet_type} and his name is {pet_name}\n\n\n")
temp_name = input("Enter Your Name\n>> ")
temp_age = int(input("Enter Your Age\n>> "))
perm_data_collection = int(input("Enter Your Yearly Savings\n>> ")) #dont worry, we won't use this later, trust us ;^)
print(f"\n\nHello {temp_name}! You are currently {temp_age} years old!\n\nIn 10 years, you will be {temp_age + 10} years "
      f"old.\n\nIf you save ${perm_data_collection} each year, in 5 years you will have saved "
      f"${perm_data_collection * 5} .\n\nYour average monthly savings is ${round(perm_data_collection / 12, 2)}.\n\n\n")
print(f"The number of seconds in January is {31*24*60*60}\n\n\n")
temp_amount = int(input("Enter The Number Of Eggs\n>> "))
print(f"\n\nThis Makes {temp_amount // 12} dozen eggs and {temp_amount % 12} left over.")
#ran on Python ver 3.10
#This is the python file for collaboration assignment.

#Step 1 Ask the user to enter his height
userHeight = float(input("Please enter your height in meters: "))

#Step 2 Ask the user to enter his weight 
userWeight = float(input("Please enter your weight in kilograms: "))

#Step 3 Calculate the BMI (Body Mass Index)
userBMI = (userWeight) / (userHeight ** 2)

#Step 4 Display the users BMI (Body Mass Index)
print("Your BMI index is " + format(userBMI, ".2f"))

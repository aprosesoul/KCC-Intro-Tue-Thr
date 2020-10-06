
# Marc - Write a function that takes in milesDriven and gallonsUsed as input. Output the milesPerGallon by printing a properly formatted message.
'''
def calculateMilesPerGallon(milesDriven, gallonsUsed):
    milesPerGallon = float (milesDriven) / float (gallonsUsed)
    print( "Miles Per a Gallon is:", format(milesPerGallon, ".2f"))

calculateMilesPerGallon(100, 5.5)
calculateMilesPerGallon(500, 31)
calculateMilesPerGallon(10, 0.5)
print()
'''
# Joss - Write a function that takes in a temperature in celsius as input. Output the temperature in fahrenheit by printing a properly formatted message.
'''
    celsius = int(input("In Celsius, what is the temperture you would like converted over to Fahrenheit?"))
    fahrenheit = celsius * 9.0/5.0 + 32 
    print("the temperature is: ", format(fahrenheit, ".2f"))

'''
# Keegan - Write a function that takes in the number of males and femalse as input. Output the percentages by printing a properly formatted message.
'''
numberMales = int(input( "How many males: "))
numberFemales = int(input( "How many females: "))
total = numberFemales + numberMales
malePercent = numberMales / total
femalePercent = numberFemales / total
print ("Percentage of males: " , format(malePercent, ".0%"))
print ("Percentage of females: " , format(femalePercent, ".0%"))
'''
# Danielle - Write a function that takes in two primary colors as input. Return the secondary color (do not print inside the function).

def primaryColorsMix(color1, color2):
    
    if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
        return("purple")
    elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
        return("orange")
    elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
        return("green")
    else:
        return("Not base colors")

print(primaryColorsMix("blue","yellow"))

print(primaryColorsMix("red","yellow"))
print(primaryColorsMix("blue","red"))
print()

# Paula - Write a function that takes in a person's age as input. Output their age categroy by printing a properly formatted message.
'''
age = int(input("Think of a person. What is their age in years? "))
if(age >= 0):
    if(age >= 0 and age <= 1):
        print("The person is an infant.")
    elif(age <= 12):
        print("The person is a child.")
    elif(age <= 19):
        print("The person is a teenager.")
    elif (age >19):
        print("The person is an adult.")
else:
    print("Invalid age")
'''
# Nicholas - Write a function that takes in a person's weight and height as input. Output the person's BMI by printing a properly formatted message.
'''
userWeight = float( input( "Please enter your weight in pounds: " ) )
userHeight = float( input( "Please enter your height in inches: " ) )
userBMI = ( userWeight * 703 ) / ( userHeight ** 2 )

if userBMI < 18.5:
    print( "A person with this BMI " + format( userBMI, ".1f" ) + \
        " is underweight")
elif userBMI < 26:
    print( "A person with this BMI " + format( userBMI, ".1f" ) + \
        " is in the optimal weight range")
else:
    print( "A person with this BMI " + format( userBMI, ".1f" ) + \
        " is Overweight")   
'''

# Jeremy - Write a function that takes in a pocket number as input. Return the color of the pocket (do not print inside the function).
'''
pocketNum = int(input('Please input a number between 0 and 36: '))
if pocketNum >= 0:
    if pocketNum < 36:
        if pocketNum == 0:
            print('The pocket is Green.')
        elif pocketNum == 1 or pocketNum == 3 or pocketNum == 5 or pocketNum == 7 or pocketNum == 9 or pocketNum == 12 or pocketNum == 14 or pocketNum == 16 or pocketNum == 18 or pocketNum == 19 or pocketNum == 21 or pocketNum == 23 or pocketNum == 25 or pocketNum == 27 or pocketNum == 30 or pocketNum == 32 or pocketNum == 34 or pocketNum == 36:
            print('The pocket is Red.')
        else:
            print('The pocket is Black.')
    else:
        print('You must enter a number less than 36')
else: 
    print('You must enter a number greater than 0')
'''

# Emma - Write a function that takes in a person's monthly budget as input. Output whether the person was under budget or over budget by printing a properly formatted message.
'''
monthlyBudget = float(input("Enter your monthly budget: "))
while(expense != "stop"):
    expense = input("Enter an expense, or if the month is over, type 'stop': ").lower().strip()
    if(expense != "stop"):
        expense = float(expense)
        monthlyBudget = monthlyBudget - expense
if(monthlyBudget > 0):
    print("You were $" + format(monthlyBudget, ',.2f') + " under budget!")
elif(monthlyBudget == 0):
    print("You were exactly on budget.")
else:
    monthlyBudget = monthlyBudget * -1
    print("You were $" + format(monthlyBudget, ',.2f') + " over budget.")
'''

# Tresha - Write a function that takes a number of points earned and total possible points as input. Output the person's grade percentage by printing a properly formatted message.
'''
points_earned = int(input("Enter points earned: "))
points_possible = int(input("Enter possible points: "))
if (points_possible != 0 and points_earned < points_possible):
  print(points_earned, "/", points_possible, "=", "{:.2%}".format(points_earned/points_possible))
'''

# Jason - Write a function that takes in an assignment score as input. Return the letter grade (do not print inside the function).
'''
score = int(input("Enter your score: "))
if (score >= 90):
    grade = "A"
elif (score >= 80):
    grade = "B"
elif (score >= 70):
    grade = "C"
elif (score >= 60):
    grade = "D"
else:
    grade = "F"
print(grade)
'''

# Jaxson - Write a function that takes in two numbers as input. Output all of the numbers between the start value and the stop value by printing a properly formatted message.
'''
start = int(input("Give a starting number: "))
stop = int(input("Give a stopping number: "))
while(start <= stop):
    print(start)
    start += 1 # increments the start variable by 1
'''
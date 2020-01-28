# Allow a user to input a dice in the classic '2d6' format
# (which would indicate 2 dice with 6 sides) and create the right random dice roll
import random
 
while True:
    roll = input("What do you want to roll?")
    if roll == "exit":
        break
    else:
        # split the string at d. So '2d6' becomes ['2', '6']
        splitRoll = roll.split("d")
        # convert the string to an integer. so ['2', '6'] becomes [2,6]
        intRoll = [int(i) for i in splitRoll]
        # set (or reset) result to 0
        result = 0
        # create random numbers for each dice rolled and add them together
        for i in range(intRoll[0]):
            result += random.randint(1, intRoll[1])
        print (result)
        result = 0
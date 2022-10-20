# Author: Henry Doan
# Project 5 Part 2
# Program will find the total amount of money the restaraunt made while the restaraunt is still open
# This restarant can only handle max of 10 people at a time, and there are only 5 foods.
# The food Choices' price are pre-made and will be listed as food choice: 1, 2, 3, 4, and 5.

import random   # Import random to create a function that picks a random customers with a limit of 10 and random food choice out of the 5
import math     # Import Math build in functions


# Create a function that adds up all the customers' choices and caculates the total amount of money the restarant made.
def calculateTotal(listOfPrices):   
    return f"${format(math.fsum(listOfPrices), '.2f')}"     


# Foods with prices
def foodPrices(chosenFood, addPrices):
    if chosenFood == 1:
        addPrices.append(3.50)
    elif chosenFood == 2:
        addPrices.append(2.00)
    elif chosenFood == 3:
        addPrices.append(1.35)
    elif chosenFood == 4:
        addPrices.append(5.65)
    elif chosenFood == 5:
        addPrices.append(4.99)


# Function to start the process of customers comming in to order food
def startCustomerOrder():   
    totalPrices = []    # a list that gathers the customers' choice of food, into an organized form to apply to caculations

    customer = random.randint(1,10)     # random amount of customers that can enter with a limit of 10
    print(f"\nThere is/are {customer} customer who have entered the restaurant\n")

    # each customer can ONLY order once
    
    while customer > 0:
        pickingFood = random.randint(1,5)   # Random choices out of the 5 options the customer picked out
        foodPrices(pickingFood, totalPrices)
        customer = customer - 1
        print(f"Customer picked option: {pickingFood}.\n")  # List the choices the customers picked
    
    
    cashOrCard = input("\nWould the customer(s) like to pay cash or card?\n(If they pay cash, they get 10-percent-OFF and round down to the nearest dollar. OR they can pay full prices with card.\n Choose one: ")
    if cashOrCard == "cash" or cashOrCard == "Cash":
        print(f"The discounted bill is: ${math.floor(math.fsum(totalPrices) * 0.9)}!\n")
    elif cashOrCard == "card" or cashOrCard == "Card":
        print(f"The total of the bill is: {calculateTotal(totalPrices)}!\n")
    else: print(f"\nCustomers are kicked out.\n")
    
# function that asks if the restarant is still open for it to ether accept new customers or close shop
def isRestaurantOpen():     
    isRestaurantOpen = input("\nIs the restaurant open?\n(Type 'yes' to continue; or type anything else to STOP)\n\nYour input: ")

    if isRestaurantOpen == "yes" or isRestaurantOpen == "Yes" or isRestaurantOpen == "y" or isRestaurantOpen == "Y":
        while isRestaurantOpen == "yes" or isRestaurantOpen == "Yes" or isRestaurantOpen == "y" or isRestaurantOpen == "Y":
            startCustomerOrder()
            isRestaurantOpen = input("Is the restaurant still open?\n(Type 'yes' to continue; or type 'no' to STOP)\n\nYour input: ")
    

isRestaurantOpen()  # Call Function
print("\nThe restaraunt is now closed.")
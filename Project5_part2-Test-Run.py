import random   # Import random to create a function that picks a random critic from the 10
import math # Import Math build in functions


totalPrice = []  # List of all the ordered foods

# Functions Definition
def calculateTotal(listOfPrices):
    return f"${math.fsum(listOfPrices)}"     # Create a function that finds the total of food did the customers orderfrom the restarant

def foodPrices(chosenFood, addPricestoList):
    if chosenFood == 1:
        addPricestoList.append(4.50)
    elif chosenFood == 2:
        addPricestoList.append(3.00)
    elif chosenFood == 3:
        addPricestoList.append(2.35)




customer = random.randint(1,10)
print(customer)

while customer > 0:
    pickingFood = random.randint(1,3)
    foodPrices(pickingFood, totalPrice)
    customer = customer - 1

print(totalPrice)
print(calculateTotal(totalPrice))


shopIsOpen = input("Is the restaurant?\n(Type 'yes' to continue; or type 'no' to STOP)\n= ")
print(shopIsOpen)
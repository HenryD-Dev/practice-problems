# Author Henry Doan
# Project 3
# Program will ask the user the delivery service, the weight of the user's package in ounce,
# the region the user is shipping to, and the delivery type.
# The program will caculate and print out the total cost based on the conditions below:
# 1. FedEx has a $2 delivery service fee, USPS has a $3 delivery service fee,
# and UPS has a $4 delivery service fee.

# 2. For all three delivery services the weight factors into the cost in this way:
# 6 ounces or fewer adds $3.25 to the cost,
# greater than 6 ounces but less than or equal to 20 ounces adds $5.50 to the cost,
# greater than 20 ounces but less than or equal to 36 ounces adds $8.50 to the cost,
# and over 36 ounces adds $15 to the cost.

# 3. Shipments to the Western region incur no region fee,
# but shipments to the Central zone double the weight fee mentioned in item 2 above,
# shipments to the Eastern zone triple the weight fee from item 2 above,
# and shipments to International delivery zones quadruple the weight fee from item 2 above.

# 4. Finally, overnight delivery type adds $9 to the cost, standard delivery type adds $6 to the cost,
# and the "get it when you get it" delivery type adds $3 to the cost.

# User Input:


deliveryService = input('Enter 1 for Federal Express\n' + 'Enter 2 for USPS\n' + 'Enter 3 for UPS\n= ')
if deliveryService.isdigit() is False: 
    print('\n*Please re-enter a whole number between 1, 2, and 3')
    deliveryService = input('Enter 1 for Federal Express\n' + 'Enter 2 for USPS\n' + 'Enter 3 for UPS\n= ')
elif int(deliveryService) < 1 or int(deliveryService) > 3: 
    print('\n*Please re-enter your number between 1, 2, and 3')
    deliveryService = input('Enter 1 for Federal Express\n' + 'Enter 2 for USPS\n' + 'Enter 3 for UPS\n= ')


packageWeight = round(float(input('\nEnter the weight of your Package in ounce (**Note: Maximum allowed shipping weight is 99 ounces per package)\n= ')))
if packageWeight <= 0 or packageWeight > 99:
    print('\n*Please re-adjust your package weight to 99 ounces or less.*')
    packageWeight = round(float(input('Enter the weight of your Package in ounce (**Note: Maximum allowed shipping weight is 99 ounces per package)\n= ')))


shippingRegion = input('\nEnter 1 for Western zone\n' + 'Enter 2 for Central zone\n' + 'Enter 3 for Eastern zone\n' + 'Enter 4 for International zone\n= ')
if int(shippingRegion) < 1 or int(shippingRegion) > 4:
    print('\n*Please re-enter your number between 1, 2, 3, and 4')
    shippingRegion = input('Enter 1 for Western zone\n' + 'Enter 2 for Central zone\n' + 'Enter 3 for Eastern zone\n' + 'Enter 4 for International zone\n= ')


deliveryType = input('\nEnter 1 for overnight/ASAP delivery\n' + 'Enter 2 for standard delivery\n' + 'Enter 3 for it gets there when it gets there\n= ')
if int(deliveryType) < 1 or int(deliveryType) > 3:
    print('\n*Please re-enter your number between 1, 2, and 3')
    deliveryType = input('Enter 1 for overnight/ASAP delivery\n' + 'Enter 2 for standard delivery\n' + 'Enter 3 for it gets there when it gets there\n= ')

# Delivery service choices 
if deliveryService == '1':
    deliveryService = 2
elif deliveryService == '2':
    deliveryService = 3
elif deliveryService == '3':
    deliveryService= 4

# Package weight costs
if packageWeight <= 6:
    packageWeight = 3.25
elif packageWeight <= 20:
    packageWeight = 5.50
elif packageWeight <= 36:
    packageWeight = 8.50
elif packageWeight > 36:
    packageWeight = 15.00

# Region shipping fee
if shippingRegion == '1':
    shippingRegion = 1
elif shippingRegion == '2':
    shippingRegion = 2
elif shippingRegion == '3':
    shippingRegion = 3
elif shippingRegion == '4':
    shippingRegion = 4

# Delivery type fee
if deliveryType == '1':
    deliveryType = 9
elif deliveryType == '2':
    deliveryType = 6
elif deliveryType == '3':
    deliveryType = 3

# Finally the total costs:
userTotal = deliveryService + (packageWeight * shippingRegion) + deliveryType

print('\n\n----- Here is the your totals -----\n')
print('\n\n Your total cost is $ ', format(userTotal, '.2f'), '\n\n')
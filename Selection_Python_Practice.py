print('Welcome to ACME inc. Online')
response1 = input('Enter 1 for store information.\n' + 'Enter 2 to see a list of departments.\n' +
                 'Enter 3 to place an order.\n' + 'Enter 4 to speak to a representative.\n')

if response1 == '1':
    print('Store Hours 8 am to 10 pm daily.\n' + 'Address: 123 Main Street, Anyville, TX\n' +
          'Phone: 512-234-5678\n' + 'website: www.acme.org\n')
elif response1 == '2':
    response2 = input('To reach Payroll, enter 1\n' + 'To reach Human Resources, enter 2\n' +
                         'To reach Customer Service, enter 3\n' + 'To reach Marketing, enter 4\n')
    if response2 == '1':
        response3 = input('You have reached the Payroll Office. We cannot come to the phone right now.\n' +
                              'To leave a message , enter 1.\n' +
                              'To have us call you back, enter 2.\n')
        if response3 == '1':
            message = input('Leave your message.\n')
            print('We have your message recorded as: ', message)
                
        elif response3 == '2':
            number = input('Leave your call back number.\n')
            print('We have your call back number as: ', number)
            print('Expect a call back within 24 hours. Have a nice day')
                    
    elif response2 == '2':
        print('Human Resources is out to lunch. Goodbye.')
                    
elif response1 == '3':
    print('You have reached the ACME online ordering system.\n')
    itemNumber = input('Enter the item number you wish to order.\n')
    quantity = input('Enter the quantity you wish to order.\n')
    print('We have your order as: Item number ', itemNumber, '\nwith a quantity of ', quantity)
elif response1 == '4':
    print('An operator will contact you shortly.\n')           
                         
        
        

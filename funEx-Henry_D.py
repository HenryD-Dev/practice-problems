# Input 5 numbers, find max, find min, find ave, display these values
import FunOne

from FunOne import FindMax, FindMin, FindAve


def main():
    # input

    num1 = int(input('Enter data value 1: '))
    num2 = int(input('Enter data value 2: '))
    num3 = int(input('Enter data value 3: '))
    num4 = int(input('Enter data value 4: '))
    num5 = int(input('Enter data value 5: '))

    print('max is ', FunOne.FindMax(num1, num2, num3, num4, num5))
    print('min is ', FunOne.FindMin(num1, num2, num3, num4, num5))
    print('ave is ', FunOne.FindAve(num1, num2, num3, num4, num5))
    
main()

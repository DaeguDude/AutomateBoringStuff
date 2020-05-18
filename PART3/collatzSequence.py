def collatz(number):
    # if number is even, print and return number // 2
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    # if number is odd, print and return 3 * number + 1
    else:
        print(number * 3 + 1)
        return number * 3 + 1
try:
    userInt = int(input('Enter number: \n'))
    returned_num = collatz(userInt)
    while returned_num != 1:
        returned_num = collatz(returned_num)
except ValueError:
    print('You must enter an integer')


    
        
    
        
    
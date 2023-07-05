def random_number(number_of_digits):

    #this give you the the smallest number for number of digits you enter 
    smallest_number = 10 ** (number_of_digits - 1)
    #this give you the the biggest number for number of digits you enter 
    Biggest_number = (10 ** number_of_digits) - 1
    # and this randomize the number between smallest number and biggest number that has number of digits that you enter
    random_number = random.randint(smallest_number, Biggest_number)
    return random_number

# this input to enter number of digits that you want in your random number
input_number_of_digits = int(input("Enter a number "))
# this to refer the number of digits to the function
num = random_number(input_number_of_digits)
print(num)

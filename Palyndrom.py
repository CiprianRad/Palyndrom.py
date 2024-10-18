# This function is the same as the one we used for all programs to get an input, the only difference is that
# it solves the case of n being negative by returning its absolute value, so it has better performace timing


def get_natural_input():
    while True:
        try:
            n = int(input("Enter an integer "))
            if n >= 0:
                return n
            else:
                return abs(n)
        except ValueError:
            print("Invalid input. Please enter an integer ")


def main():

    n = get_natural_input()
    number_list = list(str(n))  # In this line we declare a list that takes in as a string value the number n
    reversed_number_list = list(reversed(number_list))  #We reversed this list using the built in python function reversed() so that it returns its palyndrom as a string
    joined_list = ''.join(reversed_number_list)  #This joins the elements of our a list into a singular string with no spaces in between
    print("The playndrom is: " + str(joined_list))


main()

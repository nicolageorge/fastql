def try_again():
    user_input = input("Would you like to try again? y/n ")
    if user_input.lower() == "y":
        main()


def validate_inputs(input1=None, input2=None):
    # here you can add whatever validation you think is necessary
    # like the range check
    try:
        number1 = int(input1)
    except Exception:
        raise ValueError("First number must be a valid integer")

    try:
        number2 = int(input2)
    except Exception:
        raise ValueError("Second number must be a valid integer")

    if number2 == 0:
        raise ValueError("For division to be possible, second number can not be 0")

    return number1, number2


def main():
    # input step
    input1 = input("Please enter the first number:")
    input2 = input("please enter the second number:")

    # validation step
    try:
        number1, number2 = validate_inputs(input1=input1, input2=input2)
    except ValueError as e:
        print(str(e))
        try_again()
        return

    # computation step
    calculated_sum = number1 + number2
    calculated_substraction = number1 - number2
    calculated_multiplication = number1 * number2
    calculated_division = number1 / number2

    # print step
    print(f"Addition result of {number1} and {number2} is {calculated_sum}")
    print(f"Substraction result of {number1} and {number2} is {calculated_substraction}")
    print(f"Multiplication result of {number1} and {number2} is {calculated_multiplication}")
    print(f"Division result of {number1} and {number2} is {calculated_division}")
    try_again()


if __name__ == "__main__":
    main()

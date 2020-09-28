print("select an operator to begin.(Addition, Subtraction, Division, Multiplication)")
print("To quit, type quit.")
quit = False

while quit == False:
    operator = input('operator: ')
    if operator == "quit":
        print("See you next time!")
        quit = True
        break

        #if type(first_number) and type(second_number) != int:
            #print("You have made an invalid input, try agian.")

    if operator.upper() == 'ADDITION':
        print("select two numbers to add.")
        first_number = input("First number: ")
        second_number = input("Second number: ")
        answer = int(first_number) + int(second_number)
        print(f"{first_number} + {second_number} is {answer}")

    elif operator.upper() == 'SUBTRACTION':
        print("Select two numbers to subtract")
        first_number = input("First number: ")
        second_number = input("Second number: ")
        answer = int(first_number) - int(second_number)
        print(f"{first_number} - {second_number} is {answer}")

    elif operator.upper() == 'DIVISION':
        print("Select two numbers to divide.")
        first_number = input("First number: ")
        second_number = input("Second number: ")
        answer = int(first_number) / int(second_number)
        print(f"{first_number} / {second_number} is {answer}")

    elif operator.upper() == "MULTIPLICATION":
        print("Select two numbers to multiply.")
        first_number = input("First number: ")
        second_number = input("Second number: ")
        answer = int(first_number) * int(second_number)
        print(f"{first_number} * {second_number} is {answer}")

    else:
        print("You made an invalid input, try agian.")

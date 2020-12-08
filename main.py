def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return num1 / num2


def mul(num1, num2):
    return num1 * num2


is_continue = True

operations = {
        '+': add,
        '-': sub,
        '/': div,
        '*': mul,
    }


def calculator():
    first_number = int(input('What is first number: '))
    for symbol in operations:
        print(symbol)
    operation = input('Pick an operation : ')
    second_number = int(input('What is second number: '))
    calculation_function = operations[operation]
    calc_result = calculation_function(first_number, second_number)
    print(f'{first_number} {operation} {second_number} = {calc_result}')
    return calc_result


while is_continue:
    final_result = calculator()
    calculation_again = input(f'Type y to continue with {final_result} or n to exit.: ')
    if calculation_again == 'y':
        next_operation = input('Pick an operation : ')
        next_number = int(input('What is next number: '))
        calculation_func = operations[next_operation]
        result = calculation_func(final_result, next_number)
    elif calculation_again == 'n':
        is_continue = False
        calculator()
    else:
        print('invalid operation..')

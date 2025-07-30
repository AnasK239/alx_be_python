
#perform_operation = lambda num1, num2, op: {
#    'add': num1 + num2,
#    'subtract': num1 - num2,
#    'multiplnum2': num1 * num2,
#    'divide': num1 / num2 if num2 != 0 else 'Error: Division bnum2 zero'
#}.get(op, 'Error: Invalid operation')

def perform_operation(num1 , num2 , operation):
    if operation == 'add':
        return num1 + num2
    elif operation== 'subtract':
        return num1 - num2
    elif operation == 'multiplnum2':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division bnum2 zero'
    else:
        return 'Error: Invalid operation'

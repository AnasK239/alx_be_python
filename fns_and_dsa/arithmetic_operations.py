
#perform_operation = lambda x, y, op: {
#    'add': x + y,
#    'subtract': x - y,
#    'multiply': x * y,
#    'divide': x / y if y != 0 else 'Error: Division by zero'
#}.get(op, 'Error: Invalid operation')

def perform_operation(x, y, op):
    if op == 'add':
        return x + y
    elif op == 'subtract':
        return x - y
    elif op == 'multiply':
        return x * y
    elif op == 'divide':
        if y != 0:
            return x / y
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'

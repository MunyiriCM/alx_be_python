# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations based on the operation parameter.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - Result of the operation, or a string message in case of an error (e.g., division by zero)
    """
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"

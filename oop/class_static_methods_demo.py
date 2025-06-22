class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b (static method)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of a and b (class method)."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b

# Demonstration
if __name__ == "__main__":
    # Static method call
    result_add = Calculator.add(10, 5)
    print(f"Addition Result: {result_add}")

    # Class method call
    result_multiply = Calculator.multiply(10, 5)
    print(f"Multiplication Result: {result_multiply}")

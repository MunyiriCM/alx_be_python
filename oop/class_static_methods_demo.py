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
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Demonstration
if __name__ == "__main__":
    result_add = Calculator.add(10, 5)
    print(f"The sum is: {result_add}")

    result_multiply = Calculator.multiply(10, 5)
    print(f"The product is: {result_multiply}")

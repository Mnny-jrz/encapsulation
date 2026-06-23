class Operation:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("⚠️ Cannot divide by zero.")
            return None
class Calculator(Operation):
    def start(self):
        while True:
            try:
                print("\nChoose operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")

                choice = input("Enter choice (1-4): ")

                if choice not in ['1', '2', '3', '4']:
                    raise ValueError("Invalid choice. Please select 1-4.")

                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    result = self.add(a, b)
                elif choice == '2':
                    result = self.subtract(a, b)
                elif choice == '3':
                    result = self.multiply(a, b)
                elif choice == '4':
                    result = self.divide(a, b)

                if result is not None:
                    print(f"Result: {result}")

            except ValueError as e:
                print(f"Error: {e}")

            again = input("Try again? (y/n): ").lower()
            if again != 'y':
                print("Thank you!")
                break

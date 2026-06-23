class NumberStats:
    def __init__(self, filename):
        self.filename = filename
class NumberStats:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers
class NumberStats:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_min_max(self):
        numbers = self.read_numbers()
        smallest = min(numbers)
        largest = max(numbers)
        return smallest, largest
class NumberStats:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_min_max(self):
        numbers = self.read_numbers()
        smallest = min(numbers)
        largest = max(numbers)
        return smallest, largest


if __name__ == "__main__":
    stats = NumberStats('numbers.txt')
    smallest, largest = stats.find_min_max()
    print(f"🔎 Smallest number: {smallest}")
    print(f"🔎 Largest number: {largest}")
class NumberStats:
    def __init__(self, filename):
        """Initialize with the source file name."""
        self.filename = filename

    def read_numbers(self):
        """Reads integers from the source file."""
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_min_max(self):
        """Finds the smallest and largest numbers."""
        numbers = self.read_numbers()
        smallest = min(numbers)
        largest = max(numbers)
        return smallest, largest


if __name__ == "__main__":
    stats = NumberStats('numbers.txt')
    smallest, largest = stats.find_min_max()
    print(f"🔎 Smallest number: {smallest}")
    print(f"🔎 Largest number: {largest}")

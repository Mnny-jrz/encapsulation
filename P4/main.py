class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename
class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers
class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        with open(self.filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    def find_duplicates(self):
        numbers = self.read_numbers()
        duplicates = set([n for n in numbers if numbers.count(n) > 1])
        return duplicates

    def most_frequent(self):
        numbers = self.read_numbers()
        return max(set(numbers), key=numbers.count)

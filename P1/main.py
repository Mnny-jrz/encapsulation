class NumberSeparator:
    def __init__(self, source_file):
        self.source_file = source_file
class NumberSeparator:
    def __init__(self, source_file):
        self.source_file = source_file

    def read_numbers(self):
        with open(self.source_file, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

class EvenOddSeperator:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.numbers = []

    def read_number(self):
        try:
            with open(self.input_filename),
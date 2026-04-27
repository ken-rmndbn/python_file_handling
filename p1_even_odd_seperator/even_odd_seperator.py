class EvenOddSeperator:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.numbers = []

    def read_number(self):
        try:
            with open(self.input_filename, "r") as file:
                self.numbers = [int(line.strip())for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error! there is no {self.input_filename}")

    def split_and_save(self):
        if not self.numbers:
            print("There is no number to process")
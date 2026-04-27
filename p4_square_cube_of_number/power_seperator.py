class PowerSeperator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []

    def read_integers(self):
        try:
            with open(self.input_file, "r") as file:
                self.numbers = [int(line.strip()) for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error! {self.input_file} not found.")
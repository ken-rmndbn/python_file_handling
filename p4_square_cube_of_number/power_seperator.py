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

    def process_and_save(self):
        if not self.numbers:
            return

        with open("double.txt", "w") as square_file, open("triple.txt", "w") as cube_file:
            for number in self.numbers:
                square_number = number ** 2
                cube_number = number ** 3

                square_file.write(f"{square_number}\n")
                cube_file.write(f"{cube_number}\n")

        print("Processing completed for double.txt and triple.txt")

if __name__ == "__main__":
    seperator = PowerSeperator("integers.txt")
    seperator.read_integers()
    seperator.process_and_save()
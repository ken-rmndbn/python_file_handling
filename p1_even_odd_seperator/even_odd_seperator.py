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

        with open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:
            for number in self.numbers:
                if number % 2 == 0:
                    even_file.write(f"{number}\n")
                else:
                    odd_file.write(f"{number}\n")
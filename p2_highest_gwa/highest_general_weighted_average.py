class HighestGeneralWeightedAverage:
    def __init__(self, filename):
        self.filename = filename
        self. top_student = ""
        self.highest_gwa = 3.0

    def find_highest_gwa(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.split()
                    if len(parts) >= 2:
                        name = parts[0]
                        gwa = float(parts[1])

                        if gwa < self.highest_gwa:
                            self.highest_gwa = gwa
                            self.top_student = name

            self.display_result()

        except FileNotFoundError:
            print("Error gwa.txt not found")
        except ValueError:
            print("Error! Make sure the file contains only names and numbers")

    def display_result(self):
        if self.top_student:
            print(f"The student with the highest gwa is {self.top_student} with a grade of {self.highest_gwa}")
            

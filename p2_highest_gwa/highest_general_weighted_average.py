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
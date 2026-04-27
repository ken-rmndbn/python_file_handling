class MultipleLineWriting:
    def __init__(self, filename):
        self.filename = filename

    def write_entries(self):
        with open(self.filename, "w") as file:
            
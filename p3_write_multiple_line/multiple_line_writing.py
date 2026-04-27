class MultipleLineWriting:
    def __init__(self, filename):
        self.filename = filename

    def write_entries(self):
        with open(self.filename, "w") as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")
                choice = input("Are there more lines y/n? ").lower()

                if choice == "n":
                    break

        print(f"\nDone! All lines saved to {self.filename}")

if __name__ == "__main__":
    line_writing = MultipleLineWriting("mylife.txt")
    line_writing.write_entries()
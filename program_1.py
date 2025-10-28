# Program #1: Name Counter, Griffin Corniea, 10/28/25


def count_file_lines():
        with open("names.txt", "r") as file:
            lines = file.readlines()
            numLines = len(lines)

        print('In the count_file_lines function')
        print(f"There are {numLines} names.")


if __name__ == '__main__':
    count_file_lines()
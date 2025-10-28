# Program #3: Number Avrager, Griffin Corniea, 10/28/25

def sum_numbers_from_file():
    try:
        total = 0
        count = 0

        with open('numbers.txt', 'r') as file:
            for line in file:
                try:
                    num = int(line.strip())
                    total += num
                    count += 1
                except ValueError:
                    print(f"ValueError: Skipping invalid line -> '{line.strip()}'")

        print(f"Total of all numbers: {total}")
        if count > 0:
            print(f"Average: {total / count}")
        else:
            print("No valid numbers found in the file.")

    except IOError:
        print("Error: Unable to read from 'numbers.txt'. Please make sure the file exists and is accessible.")

if __name__ == '__main__':
    sum_numbers_from_file()
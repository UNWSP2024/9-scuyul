# Program #2: Rand number generator, Griffin Corniea, 10/28/25
import random

def main():
    amount = int(input("How many random numbers should the file hold (1–1000)? "))
    if amount < 1 or amount > 1000:
        print("Please enter a number between 1 and 1000.")
        return

    with open("random_numbers.txt", "w") as file:
        for i in range(amount):
            number = random.randint(1, 500)
            file.write(str(number) + "\n")
    print(f"{amount} random numbers have been written to 'random_numbers.txt'.")

if __name__ == "__main__":
    main()
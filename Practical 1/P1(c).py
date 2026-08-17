print("S087 Akshat Halwai")

try:
    n = int(input("Enter the number of values: "))

    for i in range(1 , n + 1):
        num = int(input(f"Enter number {i}: "))
        square_root = num ** 1 / 2
        print(f"Square of {num} = {square_root}")

except ValueError:
    print("Invalid input! Please enter integers only.")

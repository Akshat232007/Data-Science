print("S087 Akshat Halwai")


def swap_variables():
    Values = []
    no_of_inputs = int(input("Enter No of Elements : "))

    for i  in range(1, no_of_inputs + 1):
        inputs = Values.append(int(input(f"Enter Interger {i} : ")))

    print(Values)

    var1 = int(input("Enter Value number  to swap : "))
    var2 = int(input("Enter Value number to swap : "))

    #Swapping Variables
    Values[var1 - 1] , Values[var2 - 1] = Values[var2 - 1] , Values[var1 - 1]

    print(Values)

if __name__ == "__main__":
    swap_variables()

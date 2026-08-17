print("S087 Akshat Halwai")

a = 9
b = 10

print(f"\nThe Addition of 2 Numbers a : {a} and b : {b} are : {a + b}\n")



def sum():
    Integer = []
    Total_Sum = 0
    a = int(input("Enter No of Inputs : "))
    for i in range(1,a+1):
        Inputs = Integer.append(int(input(f"Enter Integer {i} : ")))

    print(Integer)

    for j in Integer:
        Total_Sum += j

    print(Total_Sum)

if __name__ == "__main__":
    sum()

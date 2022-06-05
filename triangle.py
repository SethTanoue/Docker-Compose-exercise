print("This is a program to print a triangle of")
row = int(input("Enter the hight of the triangle:"))
print("-----------------------------------------")
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    # empty line after each row
    print("")
for column in range(1, 21, 2):
    print(column, end=' ')
print()

for column in range(0, 110, 10):
    print(column, end=' ')
print()

for column in range(20, 0, -1):
    print(column, end=' ')
print()

number=int(input("Enter a number: "))
for column in range(0, number):
    print("*", end=' ')
print()

number=int(input("Enter a number: "))
for row in range(0, number):
    for column in range(0, row + 1):
        print("*", end=' ')
    print()


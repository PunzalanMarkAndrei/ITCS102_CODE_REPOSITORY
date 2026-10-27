size = int(input("Enter your size"))
mark = 1
for x in range (size):
    for y in range (x):
        print(mark, end= " ")
        mark += 1
    print()

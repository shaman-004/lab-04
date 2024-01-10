def print_s_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()
    for i in range(n-1, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

size = 5
print_s_pattern(size)
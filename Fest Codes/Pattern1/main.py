n = 6

# upper part of the heart
for i in range(n//2, n, 2):
    # print first spaces
    for j in range(1, n-i ,2):
        print(" ", end="")
    # print first stars
    for j in range(1, i+1, 1):
        print("*", end="")
    # print second spaces
    for j in range(1, n-i+1, 1):
        print(" ", end="")
    # print second stars
    for j in range(1, i+1, 1):
        print("*", end="")
    print()

# lower part
for i in range(n,0,-1):
    for j in range(i, n, 1):
        print(" ", end="")
    for j in range(1, i*2, 1):
        print("*", end="")
    print()
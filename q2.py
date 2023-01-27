l = int(input("Enter the Lower Limit of Range: "))
u = int(input("Enter the Upper Limit of Range: "))
n = int(input("Enter the Number: "))

for i in range(l, u + 1):
    if i % n == 0:
        print(i)

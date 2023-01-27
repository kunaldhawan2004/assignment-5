a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

if int(a) + int(b) > int(c) and int(b) + int(c) > int(a) and int(a) + int(c) > int(b):
    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The area of the triangle is: ', round(area, 2))
else:
    print("Triangle Not possible")

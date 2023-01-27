def reverse(string):
    string = string[::-1]
    return string


s = str(input("Enter The String:\n"))

print("The original string is: ")
print(s)

print('\n')

print("The reversed string is: ")
print(reverse(s))
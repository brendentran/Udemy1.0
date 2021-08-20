#The symbol ":" means up to, but not including

parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;372:036,854,775;807"
seperators = (number[1::4])
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

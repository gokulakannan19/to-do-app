password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

upper_case = False
for i in password:
    if i.isupper():
        upper_case = True
result["upper-case"] = upper_case

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")

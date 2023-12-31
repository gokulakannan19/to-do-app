value = input("Enter feet and inches: ")
def convert_meters(measures):
    value_local = measures.split(" ")
    feet = value_local[0]
    inches = value_local[1]

    meters = feet * 2 + inches * 2

    return meters

result = convert_meters(value)

if result > 1:
    print("kid can take the slide")
else:
    print("kid cannot take the slide")

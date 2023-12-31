value = input("Enter feet and inches: ")


def parse_values(measures):
    value_local = measures.split(" ")
    feet = value_local[0]
    inches = value_local[1]
    return {"feet": feet, "inches": inches}


def convert_meters(feet, inches):
    meters = feet * 2 + inches * 2
    return meters


parsed = parse_values(value)
result = convert_meters(parsed["feet"], parsed["inches"])

if result > 1:
    print("kid can take the slide")
else:
    print("kid cannot take the slide")

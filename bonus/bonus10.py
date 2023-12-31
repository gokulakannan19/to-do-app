try:
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    if width == height:
        exit("You enter a square dimension")

    area = width * height
    print(area)
except ValueError:
    print("Enter a number")
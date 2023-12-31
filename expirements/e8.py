filenames = ["a", "b", "c"]
for filename in filenames:
    file = open(f"../files/{filename}.txt", "r")
    print(file.read())

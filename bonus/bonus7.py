filenames = ["1.doc", "1.report", "1.presentation"]

new_filenames = [f'{filename.replace(".", "-", 1)}.txt' for filename in filenames]

print(new_filenames)
contents = ["All carrots were to be sliced"
            "longitudenally",
            "All carrots were reportedly sliced",
            "The slicing process was presented well"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
    file.close()
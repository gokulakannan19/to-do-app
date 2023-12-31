import zipfile
import pathlib


def compress_files(filepaths, destination_dir):
    destination_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(destination_path, "w") as archive:
        for file in filepaths:
            filepath = pathlib.Path(file)
            archive.write(file, arcname=filepath.name)


if __name__ == "__main__":
    compress_files(["bonus1.py", "bonus2_1.py"], "dest")
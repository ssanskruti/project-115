import os

source="C:/Users/91976/Downloads/xyz.png"
destination="C:/Users/91976/Downloads/abc.png"

os.rename(source,destination)

if os.path.exists(destination):
    print("Source path renamed to destination path successfully!")


import os

root = "lfw"

for root, dirs, files in os.walk(root):
    count = 0
    for filename in dirs:
        dir = f"{root}/{filename}"
        list = os.listdir(dir)
        count = len(list)
        if count >= 2:
             print(os.path.join(root, filename))
        
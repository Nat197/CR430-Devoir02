import os
import matplotlib.pyplot as mp

root = "lfw"

for root, dirs, files in os.walk(root):
    count = 0
    for filename in dirs:
        dir = f"{root}/{filename}"
        list = os.listdir(dir)
        count = len(list)
        if count >= 2:
            print(os.path.join(root, filename))
            for img in list:
                image = mp.imread(f"{dir}/{img}")
                print(image.shape)

        
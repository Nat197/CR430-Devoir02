import os
import matplotlib.pyplot as mp
import numpy as np
from tabulate import tabulate

root = "lfw"

for root, dirs, files in os.walk(root):
    count = 0
    data = []
    for filename in dirs:
        dir = f"{root}/{filename}"
        list = os.listdir(dir)
        count = len(list)
        if count >= 70:
            print(os.path.join(root, filename))

            for img in list:
                image = mp.imread(f"{dir}/{img}")
                red=np.mean(image[:,:,2])
                green=np.mean(image[:,:,1])
                blue=np.mean(image[:,:,0])
                data.append([img,red,green,blue])
                print(tabulate(data,headers=['img_name','R','G','B'],tablefmt='fancy_grid'))
            

        
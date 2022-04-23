import os
import sys
import matplotlib.pyplot as mp
import numpy as np
from tabulate import tabulate
import multiprocessing
import time

def calculRGB(root):
    start_time = time.time()
    for root, dirs, files in os.walk(root):
        count = 0   
        #Parcourir tous les fichiers dans les sous repertoire du root avec os.walk
        for filename in dirs:
            dir = f"{root}/{filename}"
            #creer une liste avec tous les fichiers dans le sous repertoire courant et mettre une valeur count sur sa longueur
            list = os.listdir(dir)
            count = len(list)
            data = []
            #Si longueur de la liste plus grand que 2 = on a plus de 2 images
            if count >= 2:
                #print(os.path.join(root, filename))
                #Parcourir tous les fichiers de ce sous repertoire
                first = True
                tempRed = None
                tempBlue = None
                tempGreen = None
                for img in list:
                    #Lire l'image et faire une moyenne de chaque valeur du RGB
                    image = mp.imread(f"{dir}/{img}")
                    red=image[:,:,0]
                    green=image[:,:,1]
                    blue=image[:,:,2]
                    if(not first):
                       tempRed = np.add(tempRed,red)
                       tempGreen = np.add(tempGreen,red)
                       tempBlue = np.add(tempBlue,red)
                    else:
                        tempRed = red
                        tempBlue = blue
                        tempGreen = green
                red = np.around(tempRed / count)
                blue = np.around(tempBlue / count)
                green = np.around(tempGreen / count)
                #print(img.shape)
                #Creation d'une image a partir d'un array
                rgb = np.zeros((250, 250, 3), dtype=np.uint8)
                rgb[..., 0] = red
                rgb[..., 1] = green
                rgb[..., 2] = blue
                mp.imsave(f'resultat/{filename}.png', rgb)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':            
    name = "lfw"
    start_time = time.time()
    t = multiprocessing.Process(target=calculRGB, args=(name,))
    t.start()

        
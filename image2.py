import os
import matplotlib.pyplot as mp
import numpy as np
from tabulate import tabulate
import time

root = "lfw"
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
            if count >= 1:
                #print(os.path.join(root, filename))
                #Parcourir tous les fichiers de ce sous repertoire
                for img in list:
                    #Lire l'image et faire une moyenne de chaque valeur du RGB
                    image = mp.imread(f"{dir}/{img}")
                    red=np.mean(image[:,:,0])
                    green=np.mean(image[:,:,1])
                    blue=np.mean(image[:,:,2])
                    data.append([red,green,blue])   
                #Lignes de test    
                #print(tabulate(data,headers=['R','G','B'],tablefmt='fancy_grid'))
                # print(np.sum(data,axis=0,dtype=np.int32)) 
                #Calcul de la moyenne RGB de toutes les images du sous-dossier
                dataSum = np.sum(data,axis=0,dtype=np.int32)
                for i in range(3):
                    dataSum[i] = dataSum[i] / count
                #print(dataSum)
                #Creation d'une image a partir d'un array
                rgb = np.zeros((255, 255, 3), dtype=np.uint8)
                rgb[..., 0] = (255-dataSum[0]) - np.arange(255)
                rgb[..., 1] = dataSum[1]
                rgb[..., 2] = (255-dataSum[2]) - np.arange(255)
                mp.imsave(f'resultat/{filename}.png', rgb)
print("--- %s seconds ---" % (time.time() - start_time))
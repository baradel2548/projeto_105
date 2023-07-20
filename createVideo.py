import cv2
import os

path = 'C:/Users/barad/Downloads/python/PRO_1-1_C105_ImagensProjeto-main/PRO_1-1_C105_ImagensProjeto-main/images'
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.jpg']:
        file_name = path +'/'+file
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,leyers=frame.shape

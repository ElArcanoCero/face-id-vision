# importing libraries
#Obtener información del proceso actual
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
import cv2
import time
import os
import psutil

process = psutil.Process()

# initializing MTCNN and InceptionResnetV1 
mtcnn0 = MTCNN(image_size=240, margin=0, keep_all=False, min_face_size=40) # keep_all=False
mtcnn = MTCNN(image_size=240, margin=0, keep_all=True, min_face_size=40) # keep_all=True
resnet = InceptionResnetV1(pretrained='vggface2').eval() 

# Using webcam recognize face

# loading data.pt file
#load_data = torch.load('Repositorio_Principal\data.pt') 
#embedding_list = load_data[0] 
#name_list = load_data[1] 

#----------------------Inicializacion de parametros----------------------------


#--------------------Face Detection-------------------------------------------------------------


#--------------------Training-------------------------------------------------------
opc = int(input("Ingrese 1 para entrenar o 2 para salir: "))
if opc == 1:
    dataset = datasets.ImageFolder('D:/UNIVERSIDAD/Diseño_Mecatronico_2/Comunicacion_Serial/imageData') # photos folder path 
    idx_to_class = {i:c for c,i in dataset.class_to_idx.items()} # accessing names of peoples from folder names

    def collate_fn(x):
        return x[0]

    loader = DataLoader(dataset, collate_fn=collate_fn)

    name_list = [] # list of names corrospoing to cropped photos
    embedding_list = [] # list of embeding matrix after conversion from cropped faces to embedding matrix using resnet

    for img, idx in loader:
        face, prob = mtcnn0(img, return_prob=True) 
        if face is not None and prob>0.92:
            emb = resnet(face.unsqueeze(0)) 
            embedding_list.append(emb.detach()) 
            name_list.append(idx_to_class[idx])        

    # save data
    data = [embedding_list, name_list] 
    torch.save(data, 'dataprueba.pt') # saving data.pt file"""
    print("Modelo entrenado con exito")

else:
    print("Imagenes extraidas con exito")
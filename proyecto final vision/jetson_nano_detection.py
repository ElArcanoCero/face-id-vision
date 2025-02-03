import tkinter as tk
from tkinter import *
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
import cv2
import os
import serial

ser = serial.Serial('COM4', 9600) # Cambia el puerto COM y la velocidad de comunicación según corresponda
num= 'A'
num1='B'
num2='C'
enviado= False
enviado1=False
enviado2=False
# abre camara y guarda datos del reconocimiento facial


    #Detectamos el rostro y exportamos los pixeles
def draw(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode, xf, yf  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        ix, iy = x, y  # Almacenamos la poscion incial en las variales
        print(ix,iy)

def reg_rostro():
            # initializing MTCNN and InceptionResnetV1 
    #mtcnn0 = MTCNN(image_size=240, margin=0, keep_all=False, min_face_size=40) # keep_all=False
    mtcnn = MTCNN(image_size=240, margin=5, keep_all=True, min_face_size=40) # keep_all=True
    resnet = InceptionResnetV1(pretrained='vggface2').eval() 

    # Using webcam recognize face

    # loading data.pt file
    load_data = torch.load('direccion del archivo aqui') 
    embedding_list = load_data[0] 
    name_list = load_data[1] 

    #----------------------Inicializacion de parametros----------------------------
    # person = str(input("Ingrese nombre de la persona: "))
    # personName = '/' + person
    cam = cv2.VideoCapture(1) 
    # cam=cv2.VideoCapture("D:/UNIVERSIDAD/diseño_mecatronico2/Faces_Recognition_project/training/porteria7.mp4") 
    #cam = cv2.VideoCapture('D:/UNIVERSIDAD/Diseño_mecatronico2/Faces_Recognition_project/training/mateo.mp4')
    count = 0
    cpu_array = []
    memory_array = []
    elapsed_time_array = []
    c = 0
    # dataPath = 'D:/UNIVERSIDAD/diseño_mecatronico2/Bot-Industries/Repositorio_Principal/image_data'
    # personPath = dataPath + personName

    # if not os.path.exists(personPath):
    #     print('Creating folder:', personPath)
    #     os.makedirs(personPath)

    #--------------------Face Detection-------------------------------------------------------------
    while True:

        ret, frame = cam.read()
        frame = cv2.resize(frame,[1920, 1080])
        frame=frame[300:700,368:1400]
        cv2.rectangle(frame,(165,0),(400,400),(0,255,0),5)
        cv2.rectangle(frame,(400,0),(650,400),(0,255,0),5)
        cv2.rectangle(frame,(650,0),(920,400),(0,255,0),5)
        
        if not ret:
            print("fail to grab frame, try again")
            break
            
        img = Image.fromarray(frame)
        img_cropped_list, prob_list = mtcnn(img, return_prob=True) 

        if img_cropped_list is not None:
            boxes, _ = mtcnn.detect(img)
                    
            for i, prob in enumerate(prob_list):
                if prob>0.90:
                    emb = resnet(img_cropped_list[i].unsqueeze(0)).detach() 
                    
                    dist_list = [] # list of matched distances, minimum distance is used to identify the person
                    
                    for idx, emb_db in enumerate(embedding_list):
                        dist = torch.dist(emb, emb_db).item()
                        dist_list.append(dist)

                    min_dist = min(dist_list) # get minumum dist value
                    min_dist_idx = dist_list.index(min_dist) # get minumum dist index
                    name = name_list[min_dist_idx] # get name corrosponding to minimum dist
                    
                    box = boxes[i] 
                    
                    original_frame = frame.copy() # storing copy of frame before drawing on it
                    
                    if min_dist<0.90:
                        frame = cv2.putText(frame, name+' '+str(min_dist), (int(box[0]), int(box[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1, cv2.LINE_AA)           
                        # os.chdir(personPath)
                        # image_path = os.path.join(personPath, f"face_{c}.png")
                        face_img = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                        if face_img is not None:
                            face_img = frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                            #aux = cv2.resize(face_img,(255,255),interpolation=cv2.INTER_CUBIC)
                            #cv2.imwrite(f"face_{c}.png", aux)         
                            frame = cv2.rectangle(frame, (int(box[0]),int(box[1])) , (int(box[2]),int(box[3])), (0,255,0), 2)
                            c += 1   
                            cv2.rectangle(frame,(165,0),(400,400),(0,255,0),5)
                            cv2.rectangle(frame,(400,0),(650,400),(0,255,0),5)
                            cv2.rectangle(frame,(650,0),(920,400),(0,255,0),5)

                            print(box[0],box[2])
                            if int(box[0]) >165 and int(box[2])<400:
                                enviado= True
                                if enviado:
                                    ser.write(num.encode())
                                    print("Primer Toriquete")
                            else:
                                enviado= False
                            if int(box[0]) >400 and int(box[2])<650:
                                enviado1= True
                                
                                ser.write(num1.encode())
                                print("Segundo Toriquete")
                            else:
                                enviado1= False
                            if int(box[0]) >650 and int(box[2])<920 :
                                enviado2= True
                                if enviado2:
                                    ser.write(num2.encode())
                                    print("Segundo Toriquete")
                            else:
                                enviado2= False
                            # if int(box[1]) >165 and int(box[1])>0 and int(box[2])<400 and int(box[3])<400:
                            #     ser.write(num.encode())
                            #     print("Primer Toriquete")
                            #     enviado= True
                            # else:
                            #     enviado= False
                            # if int(box[1]) >400 and int(box[1])>0 and int(box[2])<650 and int(box[3])<400:
                            #     print("Segundo Toriquete")
                            #     ser.write(num1.encode())
                            # if int(box[1]) >650 and int(box[1])>0 and int(box[2])<920 and int(box[3])<400:
                            #     print("Segundo Toriquete")
                            #     ser.write(num2.encode())
                    else:
                        frame = cv2.rectangle(frame, (int(box[0]),int(box[1])) , (int(box[2]),int(box[3])), (0,0,255), 2)
                    
        cv2.imshow("IMG", frame)
        cv2.namedWindow('IMG')
        cv2.setMouseCallback('IMG', draw)    
        
        k = cv2.waitKey(1)
        if k%256==27 or c >= 500: # ESC
            print('Esc pressed, closing...')
            break

    cam.release()
    cv2.destroyAllWindows()

reg_rostro()
import prediksi
import tkinter as tk
import numpy as np   
from PIL import Image, ImageTk, ImageDraw

model = prediksi.load_ai() 
window = tk.Tk()
img = Image.new(mode = "1", size = (500,500), color = 0)
tkimage = ImageTk.PhotoImage(img)
canvas = tk.Label(window, image = tkimage)
canvas.pack()
draw = ImageDraw.Draw(img)
last_point = (0,0)
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)

def draw_image(event):
    global last_point, tkimage
    current_point = (event.x, event.y)
    draw.line([last_point, current_point], fill = 255, width= 50)
    last_point = current_point
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    img_temp = img.resize((28,28))
    img_temp = np.array(img_temp)
    img_temp = img_temp.flatten()
    output = model.predict([img_temp])
    if(output[0] == 0):
       prediction.set("Letter A || Pronunciation ei")
    elif(output[0] == 1):
        prediction.set("Letter B || Pronunciation bi")
    elif(output[0] == 2):
        prediction.set("Letter C || Pronunciation si")
    elif(output[0] == 3):
       prediction.set("Letter D || Pronunciation di")
    elif(output[0] == 4):
       prediction.set("Letter E || Pronunciation i")
    elif(output[0] == 5):
       prediction.set("Letter F || Pronunciation ef")
    elif(output[0] == 6):
       prediction.set("Letter G || Pronunciation ji")
    elif(output[0] == 7):
       prediction.set("Letter H || Pronunciation eitch")
    elif(output[0] == 8):
       prediction.set("Letter I || Pronunciation ai")
    elif(output[0] == 9):
       prediction.set("Letter J || Pronunciation jey")
    elif(output[0] == 10):
       prediction.set("Letter K || Pronunciation key")
    elif(output[0] == 11):
       prediction.set("Letter L || Pronunciation el")
    elif(output[0] == 12):
       prediction.set("Letter M || Pronunciation em")
    elif(output[0] == 13):
       prediction.set("Letter N || Pronunciation en")
    elif(output[0] == 14):
       prediction.set("Letter O || Pronunciation ow")
    elif(output[0] == 15):
       prediction.set("Letter P || Pronunciation pi")
    elif(output[0] == 16):
       prediction.set("Letter Q || Pronunciation kyu")
    elif(output[0] == 17):
       prediction.set("Letter R || Pronunciation ar")
    elif(output[0] == 18):
       prediction.set("Letter S || Pronunciation es")
    elif(output[0] == 19):
       prediction.set("Letter T || Pronunciation ti")
    elif(output[0] == 20):
       prediction.set("Letter U || Pronunciation yu")
    elif(output[0] == 21):
       prediction.set("Letter V || Pronunciation vi")
    elif(output[0] == 22):
       prediction.set("Letter W || Pronunciation dabelyu")
    elif(output[0] == 23):
       prediction.set("Letter X || Pronunciation eks")
    elif(output[0] == 24):
       prediction.set("Letter Y || Pronunciation wai")
    elif(output[0] == 25):
       prediction.set("Letter A || Pronunciation zed")
    label.pack()

def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

def reset_canvas(event):
    global tkimage, img, draw
    img = Image.new(mode = "1", size = (500,500), color = 0)
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
U = 0
V = 0
W = 0
X = 0
Y = 0
Z = 0

def save_image(event):
    global A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
    img_temp = img.resize((28,28))
    if (event.char == "a"):
        img_temp.save(f"A/{A}.png")
        A += 1
    elif(event.char == "b"):
        img_temp.save(f"B/{B}.png")
        B += 1
    elif(event.char == "c"):
        img_temp.save(f"C/{C}.png")
        C += 1
    elif(event.char == "d"):
       img_temp.save(f"D/{D}.png")
       D += 1
    elif(event.char == "e"):
       img_temp.save(f"E/{E}.png")
       E += 1
    elif(event.char == "f"):
       img_temp.save(f"F/{F}.png")
       F += 1
    elif(event.char == "g"):
       img_temp.save(f"G/{G}.png")
       G += 1
    elif(event.char == "h"):
       img_temp.save(f"H/{H}.png")
       H += 1
    elif(event.char == "i"):
       img_temp.save(f"I/{I}.png")
       I += 1
    elif(event.char == "j"):
       img_temp.save(f"J/{J}.png")
       J += 1
    elif(event.char == "k"):
       img_temp.save(f"K/{K}.png")
       K += 1
    elif(event.char == "l"):
       img_temp.save(f"L/{L}.png")
       L += 1
    elif(event.char == "m"):
       img_temp.save(f"M/{M}.png")
       M += 1
    elif(event.char == "n"):
       img_temp.save(f"N/{N}.png")
       N += 1
    elif(event.char == "o"):
       img_temp.save(f"O/{O}.png")
       O += 1
    elif(event.char == "p"):
       img_temp.save(f"P/{P}.png")
       P += 1
    elif(event.char == "q"):
       img_temp.save(f"Q/{Q}.png")
       Q += 1
    elif(event.char == "r"):
       img_temp.save(f"R/{R}.png")
       R += 1
    elif(event.char == "s"):
       img_temp.save(f"S/{S}.png")
       S += 1
    elif(event.char == "t"):
       img_temp.save(f"T/{T}.png")
       T += 1
    elif(event.char == "u"):
       img_temp.save(f"U/{U}.png")
       U += 1
    elif(event.char == "v"):
       img_temp.save(f"V/{V}.png")
       V += 1
    elif(event.char == "w"):
       img_temp.save(f"W/{W}.png")
       W += 1
    elif(event.char == "x"):
       img_temp.save(f"X/{X}.png")
       X += 1
    elif(event.char == "y"):
       img_temp.save(f"Y/{Y}.png")
       Y += 1
    elif(event.char == "z"):
       img_temp.save(f"Z/{Z}.png")
       Z += 1

window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_image)
label.pack()   
window.mainloop()
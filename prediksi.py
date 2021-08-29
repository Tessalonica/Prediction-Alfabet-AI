from sklearn.neighbors import KNeighborsClassifier 
from PIL import Image
import os
import numpy as np

def load_dataset():
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    I = []
    J = []
    K = []
    L = []
    M = []
    N = []
    O = []
    P = []
    Q = []
    R = []
    S = []
    T = []
    U = []
    V = []
    W = []
    X = []
    Y = []
    Z = []
    for file in os.listdir("A"):
        img = Image.open("A/" + file)
        img = np.array(img)
        img = img.flatten()
        A.append(img)
    for file in os.listdir("B"):
        img = Image.open("B/" + file)
        img = np.array(img)
        img = img.flatten()
        B.append(img)
    for file in os.listdir("C"):
        img = Image.open("C/" + file)
        img = np.array(img)
        img = img.flatten()
        C.append(img)
    for file in os.listdir("D"):
        img = Image.open("D/" + file)
        img = np.array(img)
        img = img.flatten()
        D.append(img)
    for file in os.listdir("E"):
        img = Image.open("E/" + file)
        img = np.array(img)
        img = img.flatten()
        E.append(img)
    for file in os.listdir("F"):
        img = Image.open("F/" + file)
        img = np.array(img)
        img = img.flatten()
        F.append(img)
    for file in os.listdir("G"):
        img = Image.open("G/" + file)
        img = np.array(img)
        img = img.flatten()
        G.append(img)
    for file in os.listdir("H"):
        img = Image.open("H/" + file)
        img = np.array(img)
        img = img.flatten()
        H.append(img)
    for file in os.listdir("I"):
        img = Image.open("I/" + file)
        img = np.array(img)
        img = img.flatten()
        I.append(img)
    for file in os.listdir("J"):
        img = Image.open("J/" + file)
        img = np.array(img)
        img = img.flatten()
        J.append(img)
    for file in os.listdir("K"):
        img = Image.open("K/" + file)
        img = np.array(img)
        img = img.flatten()
        K.append(img)
    for file in os.listdir("L"):
        img = Image.open("L/" + file)
        img = np.array(img)
        img = img.flatten()
        L.append(img)
    for file in os.listdir("M"):
        img = Image.open("M/" + file)
        img = np.array(img)
        img = img.flatten()
        M.append(img)
    for file in os.listdir("N"):
        img = Image.open("N/" + file)
        img = np.array(img)
        img = img.flatten()
        N.append(img)
    for file in os.listdir("O"):
        img = Image.open("O/" + file)
        img = np.array(img)
        img = img.flatten()
        O.append(img)
    for file in os.listdir("P"):
        img = Image.open("P/" + file)
        img = np.array(img)
        img = img.flatten()
        P.append(img)
    for file in os.listdir("Q"):
        img = Image.open("Q/" + file)
        img = np.array(img)
        img = img.flatten()
        Q.append(img)
    for file in os.listdir("R"):
        img = Image.open("R/" + file)
        img = np.array(img)
        img = img.flatten()
        R.append(img)
    for file in os.listdir("S"):
        img = Image.open("S/" + file)
        img = np.array(img)
        img = img.flatten()
        S.append(img)
    for file in os.listdir("T"):
        img = Image.open("T/" + file)
        img = np.array(img)
        img = img.flatten()
        T.append(img)
    for file in os.listdir("U"):
        img = Image.open("U/" + file)
        img = np.array(img)
        img = img.flatten()
        U.append(img)
    for file in os.listdir("V"):
        img = Image.open("V/" + file)
        img = np.array(img)
        img = img.flatten()
        V.append(img)
    for file in os.listdir("W"):
        img = Image.open("W/" + file)
        img = np.array(img)
        img = img.flatten()
        W.append(img)
    for file in os.listdir("X"):
        img = Image.open("X/" + file)
        img = np.array(img)
        img = img.flatten()
        X.append(img)
    for file in os.listdir("Y"):
        img = Image.open("Y/" + file)
        img = np.array(img)
        img = img.flatten()
        Y.append(img)
    for file in os.listdir("Z"):
        img = Image.open("Z/" + file)
        img = np.array(img)
        img = img.flatten()
        Z.append(img)
    return A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

def load_ai():
    model = KNeighborsClassifier(n_neighbors = 5)
    print("[INFO] Loading Dataset")
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = load_dataset()
    print("[INFO] Loading Model")
    y_A = np.zeros(len(A))
    y_B = np.ones(len(B))
    y_C = np.ones(len(C)) * 2
    y_D = np.ones(len(D)) * 3
    y_E = np.ones(len(E)) * 4
    y_F = np.ones(len(F)) * 5
    y_G = np.ones(len(G)) * 6
    y_H = np.ones(len(H)) * 7
    y_I = np.ones(len(I)) * 8
    y_J = np.ones(len(J)) * 9
    y_K = np.ones(len(K)) * 10
    y_L = np.ones(len(L)) * 11
    y_M = np.ones(len(M)) * 12
    y_N = np.ones(len(N)) * 13
    y_O = np.ones(len(O)) * 14
    y_P = np.ones(len(P)) * 15
    y_Q = np.ones(len(Q)) * 16
    y_R = np.ones(len(R)) * 17
    y_S = np.ones(len(S)) * 18
    y_T = np.ones(len(T)) * 19
    y_U = np.ones(len(U)) * 20
    y_V = np.ones(len(V)) * 21
    y_W = np.ones(len(W)) * 22
    y_X = np.ones(len(X)) * 23
    y_Y = np.ones(len(Y)) * 24
    y_Z = np.ones(len(Z)) * 25
    X = A + B + C + D + E + F + G + H + I + J + K + L + M + N + O + P + Q + R + S + T + U + V + W + X + Y + Z
    y = np.concatenate([y_A, y_B, y_C, y_D, y_E, y_F, y_G, y_H, y_I, y_J, y_K, y_L, y_M, y_N, y_O, y_P, y_Q, y_R, y_S, y_T, y_U, y_V, y_W, y_X, y_Y, y_Z])
    model.fit(X, y)
    return model
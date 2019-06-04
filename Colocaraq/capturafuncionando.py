import cv2
classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
video = cv2.VideoCapture(0)
encerrar = True
amostra = 1
numeroAmostras = 25
id = input('Digite seu identificador')
largura,altura = 220, 220 # Pixels
print("Iniciando Câmera...")
while encerrar == True:
    connectado, imagem = video.read()
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, #Recebe a detecção em tempo real da imagem
                                                     scaleFactor=1.5, # Tamanho da escala
                                                      minSize= (50, 50)) # Tamanho minimo p/ detectar faces
    for(x,y,l,a) in facesDetectadas: # Dentro desse for ele vai realizar o que for programado enquanto detecta faces
        cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 0), 2) # Retangulo desenhado
        #print('Achei um rosto!!')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura,altura))
            cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("[Foto " + str(amostra) + "capturada com sucesso]")
            amostra += 1

    cv2.imshow('Reconhecimento De Imagem', imagem)
    if amostra >= numeroAmostras + 1:
        break
    if cv2.waitKey(1) == ord('w'):
        encerrar = False
        video.release() # Libera espaço na memori
        cv2.destroyAllWindows() #Destroi as janelas



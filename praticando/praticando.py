import cv2
video = cv2.VideoCapture(0)
encerrar = True
while encerrar == True:
    imagem,frame = video.read(0)
    cv2.imshow('test',frame)
    if cv2.waitKey(1)==ord('q'):
        encerrar = False
        cv2.destroyAllWindows()
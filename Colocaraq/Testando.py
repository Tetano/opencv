print('python')
import cv2
video = cv2.VideoCapture(0)
while True:
    connectado, frame = video.read()
    cv2.imshow('Reconhecimento De Imagem', frame)

    if cv2.waitKey(1) == ord('q'):
        break
        video.release()
        cv2.DestroyAllWindowns

import cv2

cap = cv2.VideoCapture(0)

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480

fourcc = cv2.VideoWriter_fourcc(*'XVID')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.ViderWriter('output.avi', fourcc, fps, (width, height))

recording = True

while recording:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27: # ESC
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
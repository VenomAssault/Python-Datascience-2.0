import cv2
# webcam1 -> 0 idx
# webcam2 -> 1 idx
file = 'computervision/sample_vid2.mp4' # <= 1
camera = cv2.VideoCapture(file)
while True:
    state, frame = camera.read() # frame -> imagecaptured,state -> boolean
    if not state:
        print("could not access video")
        break # if state is false stop the loop
    cv2.imshow('camera window', frame)
    if cv2.waitKey(20) == ord('q'): # if q is presented stop the loop
        break
camera.release()
cv2.destroyAllWindows()

import cv2,os
import mediapipe as mp 

# webcam1 -> 0 idx
# webcam2 -> 1 idx
file = 'computervision/sample_vid2.mp4' # <= 1
if not os.path.exists(file):
    print('video file not found')
camera = cv2.VideoCapture(file)
with mp.solutions.pose.Pose(
    model_complexity=0,
    min_detection_confidence = .5,
    min_tracking_confidence=.5) as pd :
    while True:
        state, frame = camera.read() # frame -> imagecaptured,state -> boolean
        if not state:
            print("could not access video")
            break # if state is false stop the loop
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pd.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks,
                mp.solutions.pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp.solutions.drawing_styles.get_default_pose_landmarks_style())
        cv2.imshow('camera window',frame)
        if cv2.waitKey(20) == ord('q'): # if q is presented stop the loop
            break
camera.release()
cv2.destroyAllWindows()
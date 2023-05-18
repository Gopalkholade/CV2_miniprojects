import cv2
import mediapipe as mp

cap = cv2.VideoCapture("task_4_video.mp4")

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(static_image_mode=False,
                    min_detection_confidence = 0.5,
                    min_tracking_confidence = 0.5)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Outputs/output_task_4.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        mp_drawing.draw_landmarks(frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
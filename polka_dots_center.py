import cv2
import numpy as np

# Define the HSV range for green color
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])

# Read the video file
cap = cv2.VideoCapture('task_2_video.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Outputs/task_2_output.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    if ret:
        # Convert the frame from BGR color space to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image to get only green color
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Find contours of the green polka dots
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw a red dot at the center of each green polka dot
        for contour in contours:
            (x,y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x),int(y))
            radius = int(radius*.1)
            cv2.circle(frame,center,radius,(0,0,255),3)

        # Write the frame with red dots to output video file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
import cv2
import time
import numpy as np

cap = cv2.VideoCapture('input/video_1.mp4')

# get the video frames' width and height for proper saving of videos
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# create the `VideoWriter()` object
out = cv2.VideoWriter('output/video_result_1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# detect objects in each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        image = frame

        # cv2.imshow('image', image)
        out.write(image)
        # if cv2.waitKey(10) & 0xFF == ord('q'):
        #     break
    else:
        break

cap.release()
cv2.destroyAllWindows()

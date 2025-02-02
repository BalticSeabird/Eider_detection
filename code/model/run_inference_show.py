import pandas as pd
from pathlib import Path 
from ultralytics import YOLO
import os 
import sys
import cv2

# Load a pretrained YOLO model
model = YOLO("models/best21.pt")

vid = "/Users/jonas/Downloads/vid/NVR_Hien_EJDER7_2024-05-16_07.00.00_001000_001200.mp4"


# Run inference using the pretrained model and the inout video


cap = cv2.VideoCapture(vid)

writer = cv2.VideoWriter('out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10.0, (640,360))

while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.predict(vid, 
                    stream=True, 
                    save = False,
                    show = True)

        # Get the boxes and track IDs
        boxes = results[0].boxes.xywh.cpu()
    
        # Visualize the results on the frame
        annotated_frame = results[0].plot(line_width=1)

        # Display the annotated frame
        cv2.imshow("YOLOv11 eiders", annotated_frame)
        writer.write(annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
writer.release()
cap.release()
cv2.destroyAllWindows()


  
# Run example 
# python3 code/yolov8/yolo_inference_multiple.py
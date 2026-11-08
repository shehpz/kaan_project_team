""" 
1. Initialize the webcam using OpenCV (cv2.VideoCapture(0)).
2. Load the YOLO model (yolov11n.pt).
3. Inside a loop:
    1. Read a frame from the webcam
    2. Run YOLO detection on the frame
    3. Draw bounding boxes and labels
    4. Display the processed frame
4. Exit the program when the user presses Q. """

import cv2
import time # calculate FPS
from ultralytics import YOLO

#https://github.com/niconielsen32/opencv-python-tutorials/blob/main/21_object_detection_ultralytics/README.md



old_frame_time = 0
new_frame_time = 0

def detect_webcam(model_path='yolo11n.pt'):
    # Load the YOLO model
    model = YOLO(model_path)

    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # Run object detection on the frame
        results = model(frame)

        # Draw bounding boxes and labels on the frame
        annotated_frame = results[0].plot()
        
        frame_count = 0
        start_time = time.time()
        
        fps = 1 / (time.time() - start_time)

        cv2.putText(annotated_frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        frame_count += 1
        

        # Display the processed frame
        cv2.imshow('Webcam Live Detection', annotated_frame)

        # Exit the loop when 'Q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    detect_webcam()
    
import cv2
import time # calculate FPS
from ultralytics import YOLO

#https://github.com/niconielsen32/opencv-python-tutorials/blob/main/21_object_detection_ultralytics/README.md





def detect_webcam(model_path='yolo11n.pt', now_time = time.time):
    # Load the YOLO model
    model = YOLO(model_path)

    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    old_frame_time = 0  # Initialize old frame time for FPS calculation
    new_frame_time = 0  # Initialize new frame time for FPS calculation

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
        
        # Calculate FPS
        
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - old_frame_time) if (new_frame_time - old_frame_time) > 0 else 0
        old_frame_time = new_frame_time 
        
            
        
        
        # Display FPS on the frame
        cv2.putText(annotated_frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        

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
    
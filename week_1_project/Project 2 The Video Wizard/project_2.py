import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    # Read a frame
    ret, frame = cap.read()
    
    if not ret:
        print("Not find frame")
        break
    
    # Process frame here
    cv2.imshow('Video', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
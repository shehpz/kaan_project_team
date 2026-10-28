import cv2


print("-----------------")
print("1- Live Video.")
print("2- Video player with users video.")
print("-----------------")
start_value = int(input("Which do you want?"))

if start_value == 1:
    
    #https://www.geeksforgeeks.org/python/python-opencv-capture-video-from-camera/
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = cam.read()

        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cv2.destroyAllWindows()
    
elif start_value == 2:
    
    path = input("Enter video path")
    
    video_capture = cv2.VideoCapture(path)
    
    while True:
        ret,frame = video_capture.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow("Video Frames", frame)
        cv2.waitKey(2)
        break

else:
    print("Wrong value app closing...")
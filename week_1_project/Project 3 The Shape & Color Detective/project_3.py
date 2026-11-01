import cv2

def show_menu():
    print("-----------------")
    print("1- Live Video.")
    print("2- Video player with users video.")
    print("-----------------")

def play_video(video_path):
    
    # If reference value is video path on cv2.VideoCapture(reference), on the path video will be open.
    video_capture = cv2.VideoCapture(video_path)

    #we can reach parameters this links;
    #https://docs.opencv.org/4.13.0/d7/dfc/group__highgui.html#gab7aed186e151d5222ef97192912127a4
    #https://docs.opencv.org/4.13.0/d7/dfc/group__highgui.html#ga89e7806b0a616f6f1d502bd8c183ad3e
    window_name = "Video Frames"
    cv2.namedWindow(window_name)
    
    
    #https://www.geeksforgeeks.org/python/how-to-get-properties-of-python-cv2-videocapture-object/
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    try:
        if not video_capture.isOpened():
            print("Not open video.")
            return

        while video_capture.isOpened():
            received, frame = video_capture.read()
            
            if not received:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            
            #https://docs.opencv.org/4.13.0/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670
            #we drawing circle on the center.
            cv2.circle(frame, center=(frame_width//2,frame_height//2), radius=30, color=(250,0,0),thickness=2)

            #https://www.geeksforgeeks.org/python/python-opencv-cv2-rectangle-method/
            #we drawing rectangel on top left corner.
            
            cv2.rectangle(frame, (5,5), (100,40), (255,0,0),3,)
            
            #we text 
            cv2.putText(frame,"EX.",(7,37),cv2.FONT_HERSHEY_SIMPLEX, 1, (250,0,0),2)
            
            #https://docs.opencv.org/4.13.0/dc/da5/tutorial_py_drawing_functions.html#autotoc_md1293
            # We define lin_xy_point out of while loop so every painting on window we don't lose polyline.
            # We use a 'for' loop to draw a straight line.
           
            
            cv2.imshow(window_name, frame)

            if cv2.waitKey(25) == ord("q"):
                break   
            #When we press s save frame img.
            elif cv2.waitKey(25) == ord("s"):
                cv2.imwrite("Example.png", frame)
                print("Screenshot is saved.")
    finally:
        video_capture.release()
        cv2.destroyAllWindows()



def main():
   
    show_menu()
    start_value = int(input("Which do you want?"))

    if start_value == 1:
        play_video(0)
    elif start_value == 2:
        video_path = input("Enter video path: ")
        play_video(video_path)
    else:
        print("Wrong value app closing...")


if __name__ == "__main__":
    main()

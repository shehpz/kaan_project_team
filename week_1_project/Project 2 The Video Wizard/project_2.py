import cv2
import numpy as np

drawing_mode = False
line_xy_points = []

#Here we show menu on terminal.
def show_menu():
    print("-----------------")
    print("1- Live Video.")
    print("2- Video player with users video.")
    print("-----------------")

def mouse_callback(event, x, y, flags, param):
    #we define global cause can be use out of function.
    global drawing_mode, line_xy_points

    #Here we define mouse event callback if callback is leftbuttondown so we left click then if we moveing mouse drawing mode is true and 
    # we add x,y poind to line_xy_points than if moment at left click up, drawing mode is false. 
    #This we reach event to this link https://docs.opencv.org/4.13.0/d0/d90/group__highgui__window__flags.html#ga927593befdddc7e7013602bca9b079b0
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_mode = True
        line_xy_points.append((x, y))
    elif event == cv2.EVENT_MOUSEMOVE and drawing_mode:
        line_xy_points.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing_mode = False

#This project need to made function by funcition cause we dont use it's will be difficult.
#We learn how can we use video player on cv2 and we found every frame image join by self than result is video.  
#This topic we need to two main method; 1- Live camera or 2- Video on computer. So I made 2 function for this topic.
#This think ı found on https://github.com/niconielsen32/opencv-python-tutorials/tree/main/10_video_basics.



def play_video(video_path):
    
    # If reference value is video path on cv2.VideoCapture(reference), on the path video will be open.
    video_capture = cv2.VideoCapture(video_path)

    #we can reach parameters this links;
    #https://docs.opencv.org/4.13.0/d7/dfc/group__highgui.html#gab7aed186e151d5222ef97192912127a4
    #https://docs.opencv.org/4.13.0/d7/dfc/group__highgui.html#ga89e7806b0a616f6f1d502bd8c183ad3e
    window_name = "Video Frames"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)
    
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
            for i in range(1, len(line_xy_points)):
                if line_xy_points[i -1] is not None and line_xy_points[i] is not None:
                    cv2.line(frame, line_xy_points[i -1], line_xy_points[i], (255,0,0), 4)
            
            
            cv2.imshow(window_name, frame)

            if cv2.waitKey(25) == ord("q"):
                break
            elif cv2.waitKey(25) == ord("c"):
                line_xy_points.clear()
                print("Drawing cleaned up.")
                
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

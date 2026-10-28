import cv2
import numpy as np

# Global variables for interactive drawing (Task 4)
drawing_mode = False
canvas_points = []

def mouse_callback(event, x, y, flags, param):
    """
    Mouse callback function to capture user clicks and draw on screen.
    """
    global drawing_mode, canvas_points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_mode = True
        canvas_points.append((x, y))
    elif event == cv2.EVENT_MOUSEMOVE and drawing_mode:
        canvas_points.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing_mode = False

def process_video_stream(source):
    """
    Reads video frames from webcam or file, draws shapes/text, 
    and handles interactive mouse/keyboard events.
    """
    global canvas_points

    video_capture = cv2.VideoCapture(source)

    if not video_capture.isOpened():
        print(f"Hata: Video kaynagi ({source}) acilamadi.")
        return

    # Task 3: Get video frame dimensions
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Task 4: Set mouse callback function on the display window
    window_name = "Project 2 - Video Wizard"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)

    screenshot_counter = 1

    print("\n--- Kontrol Tuslari ---")
    print("'s' -> Ekran goruntusu kaydet")
    print("'c' -> Ekrandaki cizimleri temizle")
    print("'q' -> Cikis yap\n")

    while True:
        ret, current_frame = video_capture.read()

        # Break loop if video file ends or stream fails
        if not ret:
            print("Video akisi sona erdi veya cerceve okunamadi.")
            break

        # Task 3: Draw shapes (rectangles and circles) and text on video frames
        # Rectangle overlay at top-left
        cv2.rectangle(current_frame, (20, 20), (280, 80), (0, 0, 0), -1)
        cv2.rectangle(current_frame, (20, 20), (280, 80), (0, 255, 0), 2)
        
        # Text overlay
        cv2.putText(current_frame, "REC - LIVE FEED", (30, 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Draw target circle at frame center
        center_x, center_y = frame_width // 2, frame_height // 2
        cv2.circle(current_frame, (center_x, center_y), 30, (0, 0, 255), 2)

        # Task 4: Draw interactive user lines from mouse input
        for idx in range(1, len(canvas_points)):
            if canvas_points[idx - 1] is not None and canvas_points[idx] is not None:
                cv2.line(current_frame, canvas_points[idx - 1], canvas_points[idx], (255, 0, 0), 4)

        # Display final processed frame
        cv2.imshow(window_name, current_frame)

        # Task 5: Capture keyboard inputs
        key = cv2.waitKey(30) & 0xFF

        # Exit application
        if key == ord('q'):
            print("Kullanici tarafindan cikis yapildi.")
            break

        # Save screenshot
        elif key == ord('s'):
            filename = f"screenshot_{screenshot_counter}.png"
            cv2.imwrite(filename, current_frame)
            print(f"Ekran goruntusu kaydedildi: {filename}")
            screenshot_counter += 1

        # Clear drawn lines
        elif key == ord('c'):
            canvas_points.clear()
            print("Ekrandaki cizimler temizlendi.")

    # Release video stream and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

def main():
    print("=== PROJECT 2: THE VIDEO WIZARD ===")
    print("1 - Canli Webcam Akisi")
    print("2 - Video Dosyasi Oynat")
    
    # Rule: Get user selection via keyboard
    choice = input("Lutfen secim yapiniz (1 veya 2): ").strip()

    if choice == '1':
        # Task 1: Access webcam using device index 0
        process_video_stream(0)
    elif choice == '2':
        # Task 2: Read video file path from user input
        video_path = input("Lutfen video dosyasinin yolunu giriniz (orn: sample.mp4): ").strip()
        process_video_stream(video_path)
    else:
        print("Gecersiz secim yapildi.")

if __name__ == "__main__":
    main()
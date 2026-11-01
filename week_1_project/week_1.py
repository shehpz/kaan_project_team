import cv2
import numpy as np

def detect_shape(contour):
    """
    Approximates contour shape and returns the shape name (Bonus Task).
    """
    # Calculate perimeter of contour
    perimeter = cv2.arcLength(contour, True)
    # Approximate polygon curve with epsilon accuracy
    approx_polygon = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    
    vertices_count = len(approx_polygon)
    
    if vertices_count == 3:
        return "Triangle"
    elif vertices_count == 4:
        # Check aspect ratio to distinguish Square vs Rectangle
        x, y, w, h = cv2.boundingRect(approx_polygon)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif vertices_count > 4:
        return "Circle"
    return "Unknown"

def process_frame(frame):
    """
    Applies HSV color filtering, contour detection, noise filtering, 
    bounding box drawing, and shape classification.
    """
    # Task 1: Convert BGR image to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Task 1: Define color thresholds for target object (e.g., Bright Green / Pen)
    # Adjust lower and upper HSV boundaries according to target object color
    lower_color = np.array([35, 50, 50])
    upper_color = np.array([85, 255, 255])

    # Task 1: Create binary mask using cv2.inRange
    color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    # Optional Morphological Operations to reduce noise in binary mask
    kernel = np.ones((5, 5), np.uint8)
    color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, kernel)

    # Task 2: Find contours in the thresholded binary mask
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = None
    max_area = 0

    # Task 3: Filter contours based on area threshold to remove noise
    min_area_threshold = 500  # Threshold to suppress small noises

    for contour in contours:
        contour_area = cv2.contourArea(contour)
        
        if contour_area > min_area_threshold:
            # Task 2: Draw detected valid contours on frame
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

            # Bonus Task: Detect specific shape (Triangle, Square, Circle)
            shape_name = detect_shape(contour)

            # Track largest object contour
            if contour_area > max_area:
                max_area = contour_area
                largest_contour = contour

    # Task 4: Draw bounding box around the largest detected object
    if largest_contour is not None:
        x, y, width, height = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 3)

        # Bonus Task: Display shape name on the detected largest object
        detected_shape = detect_shape(largest_contour)
        text_label = f"Target ({detected_shape})"
        cv2.putText(frame, text_label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    return frame, color_mask

def main():
    print("=== PROJECT 3: SHAPE & COLOR DETECTIVE ===")
    print("1 - Görsel Dosyası Üzerinde Nesne Tespiti")
    print("2 - Canlı Webcam Üzerinde Nesne Tespiti")
    
    # Rule: Get user input via keyboard
    choice = input("Lutfen secim yapiniz (1 veya 2): ").strip()

    if choice == '1':
        # Rule: Ask file path from user
        image_path = input("Lutfen gorsel dosyasinin yolunu giriniz (orn: test.jpg): ").strip()
        input_image = cv2.imread(image_path)

        if input_image is None:
            print(f"Hata: '{image_path}' konumundaki gorsel yuklenemedi.")
            return

        processed_frame, mask_frame = process_frame(input_image)

        cv2.imshow("Original with Detection", processed_frame)
        cv2.imshow("HSV Color Mask", mask_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == '2':
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            print("Hata: Webcam acilamadi.")
            return

        print("\nCanli tespit baslatildi. Cikis yapmak icin 'q' tusuna basiniz.\n")

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            processed_frame, mask_frame = process_frame(frame)

            cv2.imshow("Live Shape & Color Detection", processed_frame)
            cv2.imshow("Color Mask", mask_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    else:
        print("Gecersiz secim yapildi.")

if __name__ == "__main__":
    main()
import cv2
import numpy as np

def show_menu():
    print("-----------------")
    print("1- Enter Image path:")
    print("-----------------")
    
def detect_shape(contour):
    #https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
    #https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html#gaa1e7f8b9d5e6f2c1a5b8f3e2c1e1f3e2
    #https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html
    
    #We define shape_name as "Unknown" by default.
    #Then we calculate the perimeter of the contour using cv2.arcLength. 
    #Next, we approximate the contour to a polygon using cv2.approxPolyDP, 
    #which simplifies the contour based on the specified precision (0.04 * perimeter).
    #We count the number of vertices in the approximated polygon to determine the shape. 
    #If there are 3 vertices, it's a triangle; if 4, we check the aspect ratio to distinguish between a 
    #square and a rectangle; if more than 4, we classify it as a circle. 
    #Finally, we return the detected shape name.
    shape_name = "Unknown"
    perimeter = cv2.arcLength(contour, True)
    approx_polygon = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    vertices_count = len(approx_polygon)
    
    if vertices_count == 3:
        shape_name = "Triangle"
    elif vertices_count == 4:
        # Check aspect ratio to distinguish Square vs Rectangle
        x, y, w, h = cv2.boundingRect(approx_polygon)
        aspect_ratio = float(w) / h
        # If the aspect ratio is approximately 1 (between 0.95 and 1.05), 
        # we classify it as a square; otherwise, it's a rectangle.
        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    elif vertices_count > 4:
        shape_name = "Circle"
        
    return shape_name

def largest_contour_x(contours):
    #https://docs.opencv.org/4.x/d7/d00/tutorial_meanshift.html

    
    #We define largest_contour as None and max_area as 0. 
    #Then we iterate through each contour in the contours list, calculating its area using cv2.contourArea. 
    #If the area is greater than the current max_area, we update max_area and set largest_contour to the current contour. 
    #Finally, we return the largest_contour found.
    
    global largest_contour
    largest_contour = None
    max_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            largest_contour = contour

    return largest_contour
    
def play_image(image_path):
    image = cv2.imread(image_path)
    original_image = image.copy()
      
    # Convert the image to HSV color space for color detection.
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #we are defining the lower and upper bounds for the green color in HSV space.
    # Define color ranges for green in HSV space.
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    
    # Convert the image to grayscale and apply Canny edge detection.
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection to the grayscale image to highlight edges.
    edged_image = cv2.Canny(grayscale_image, 100, 200)
    
    #https://www.geeksforgeeks.org/python-find-and-draw-contours-using-opencv-python/
    contours, hierarchy = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    
    global largest_contour
    largest_contour = largest_contour_x(contours)
    
    
    for contour in contours:
        # Filter contours based on area to remove noise.
        area = cv2.contourArea(contour)
        if area <= 100:
            # Ignore small contours that are likely noise.
            continue

        # Highlight the largest contour; use identity comparison because
        # comparing NumPy arrays with == produces an array of booleans.
        is_largest = largest_contour is not None and contour is largest_contour
        color = (0, 0, 255) if is_largest else (0, 255, 0)
        thickness = 3 if is_largest else 2
        cv2.drawContours(image, [contour], -1, color, thickness)

        shape_name = detect_shape(contour)
        x, y, w, h = cv2.boundingRect(contour)
        label = f"Largest Shape: {shape_name}" if is_largest else shape_name
        # Place the label beside the contour's upper edge, keeping it inside the image.
        label_y = y - 10 if y >= 20 else y + h + 20
        cv2.putText(image, label, (x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Draw contours on a copy of the image for visualization without mutating the
    # original drawing result used for display.
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
    
    print(f"Number of contours detected: {len(contours)}")
    
    # Use bitwise operations to extract the colored regions from the original image using the masks.
    green_result = cv2.bitwise_and(image, image, mask=green_mask)
    
    
    
    if image is None:
        print(f"Error: Could not load image from '{image_path}'.")
        return
    
    
    
    
    cv2.imshow("Original Image", original_image)
    cv2.waitKey(0)
    cv2.imshow("Green Color Detection", green_result)
    cv2.waitKey(0)
    cv2.imshow("Edged Image", edged_image)
    cv2.waitKey(0)
    cv2.imshow("Image with Contours", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def main():
   
    show_menu()
    image_path = input("Enter image path: ")
    play_image(image_path)



if __name__ == "__main__":
    main()

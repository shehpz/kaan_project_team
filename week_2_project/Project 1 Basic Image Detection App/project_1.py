
import cv2
from ultralytics import YOLO

#https://www.geeksforgeeks.org/machine-learning/object-detection-using-yolov8/
#https://github.com/niconielsen32/opencv-python-tutorials/blob/main/21_object_detection_ultralytics/README.md
def detect_image(image_path, model_path='yolo26n.pt'):
    # Load the YOLO model
    model = YOLO(model_path)

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image from {image_path}")
        return

    # Run object detection
    results = model(image)

    result = results[0]  # Get the first result (assuming single image input)
    
    boxes = result.boxes
    
    print("Detected Objects:")
    
    # Loop through detected boxes and print class names, confidence scores, and bounding box coordinates
    for box in boxes:
        class_id = int(box.cls[0])  # Get the class ID
        class_name = model.names[class_id]  # Get the class name
        confidence = float(box.conf[0])  # Get the confidence score
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates

        print(f"Class: {class_name}, Confidence: {confidence:.2f}, Bounding Box: ({x1}, {y1}), ({x2}, {y2})")
    
    # Draw bounding boxes on the image
    annotated_image = results[0].plot()

    # Save and display the result image
    output_image_path = 'result.jpg'
    cv2.imwrite(output_image_path, annotated_image)
    cv2.imshow('Detected Objects', annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    # Example usage
    input_path = input("Enter the path of the image file: ").strip()
    
    if input_path:
        detect_image(input_path)
    else:
        print("No path provided. Please run the script again with a valid image path.") 
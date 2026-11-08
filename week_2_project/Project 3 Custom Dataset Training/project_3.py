
#https://docs.ultralytics.com/datasets/detect/open-images-v7
#https://docs.ultralytics.com/yolov5/tutorials/train-custom-data

from ultralytics import YOLO

def train_custom_dataset(data_yaml_path, model_path, epochs, batch_size):
    model = YOLO(model_path)
    
    # Train the model on the custom dataset
    results = model.train(
        data=data_yaml_path, 
        epochs=epochs, 
        batch=batch_size
    )
    return results

if __name__ == "__main__":
    # Get user input for data.yaml path and pre-trained model path
    data_yaml_path = input("Enter the path to your data.yaml file: ").strip()
    model_path = input("Enter the path to the pre-trained YOLO model (e.g., yolov8n.pt): ").strip()
    # Get user input for training parameters
    epochs = int(input("Enter the number of training epochs (default 100): ") or 100)
    # Get user input for batch size
    batch_size = int(input("Enter the batch size (default 16): ") or 16)

    # Check if both paths are provided
    if data_yaml_path and model_path:
        print(train_custom_dataset(data_yaml_path, model_path, epochs, batch_size))
    else:
        print("Please provide valid paths for both data.yaml and the pre-trained YOLO model.")
        
    

        
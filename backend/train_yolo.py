from ultralytics import YOLO

def main():
    print("Loading base YOLOv8n model...")
    model = YOLO("yolov8n.pt")  # load a pretrained model
    
    print("Training on local coastal debris dataset...")
    # Train the model for a few epochs (just for demo purposes)
    results = model.train(
        data="dataset/data.yaml",
        epochs=5,
        imgsz=640,
        batch=1,
        project="runs/detect",
        name="marine_debris_model",
        exist_ok=True
    )
    
    print("Training complete! Best weights saved to: runs/detect/marine_debris_model/weights/best.pt")

if __name__ == "__main__":
    main()



# Importing the required libraries
from roboflow import Roboflow
from ultralytics import YOLO
from clearml import Task

# Creating an instance of the Roboflow class
#rf = Roboflow(api_key="2Z8LedwxqBlKAbVYyz8T")
#project = rf.workspace("ai-course-2024").project("eiders2")
#version = project.version(1)
#dataset = version.download("yolov11")
                

# Initialize ClearML task
task = Task.init(project_name="YOLOv11 Training Eiders", task_name="YOLOv11 Model Eiders")

# Load a COCO-pretrained YOLO11n model
model = YOLO("models/yolo11m.pt")

# Train the model on the dataset for 50 epochs
results = model.train(data="Eiders2-1/data.yaml", epochs=50, imgsz=1280, device = [1])

# Log the results to ClearM
task.upload_artifact('training_results_dataset_v1', results)

# Save the model
model.save('models/eider_model_v01.pt')

# Close the ClearML task
task.close()

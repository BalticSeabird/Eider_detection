

# Importing the required libraries
from roboflow import Roboflow
from ultralytics import YOLO
from clearml import Task
import torch

torch.cuda.empty_cache()

# Creating an instance of the Roboflow class
#rf = Roboflow(api_key="2Z8LedwxqBlKAbVYyz8T")
#project = rf.workspace("ai-course-2024").project("eiders2")
#version = project.version(2)
#dataset = version.download("yolov11")

#PYTORCH_CUDA_ALLOC_CONF=expandable_segments:Tr          

# Initialize ClearML task
task = Task.init(project_name="YOLOv11 Training Eiders", task_name="YOLOv11 Model Eiders")

# Load a COCO-pretrained YOLO11n model
model = YOLO("models/yolo11m.pt")

# Train the model on the dataset for 50 epochs
results = model.train(data="Eiders2-2/data.yaml", batch=8, epochs=100, imgsz=1280, device = 0)

# Log the results to ClearML
task.upload_artifact('training_results_dataset_v2', results)

# Save the model
model.save('models/eider_model_v01.pt')

# Close the ClearML task
task.close()

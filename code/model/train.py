

# Importing the required libraries
from roboflow import Roboflow

# Creating an instance of the Roboflow class
rf = Roboflow(api_key="2Z8LedwxqBlKAbVYyz8T")
project = rf.workspace("ai-course-2024").project("eiders2")
version = project.version(1)
dataset = version.download("yolov11")
                



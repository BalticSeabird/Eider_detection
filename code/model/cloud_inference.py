


from inference_sdk import InferenceHTTPClient

# create an inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="2Z8LedwxqBlKAbVYyz8T"
)

# run inference on a local image
print(CLIENT.infer(
    "data/ims/EjderNVR_EJDER1_2024-05-07_20.00.00_002900_003100_1800.png", 
    model_id="eiders2/1"
))


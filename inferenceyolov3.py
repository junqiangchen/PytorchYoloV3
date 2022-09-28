from models import *

if __name__ == "__main__":
    yolov3 = yolov3inferenceModel(weights=r'log/train/exp2/weights/best.pt')
    image = cv2.imread(r'D:\challenge\project\PytorchYoloModel\data\testimages\peoples.png')
    yolov3.inference(image)

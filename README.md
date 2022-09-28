# PytorchYoloV3

# Object Detection Yolov3 Model
> There is Yolov3 Model NetWorks of 2D Object Detection
>[Original link](https://github.com/ultralytics/yolov3)

## How to Use
i have implemented Yolov3 Train and inference stage with pytorch1.10.0.

this is very easy to use it
>yolov3 train can run trainyolov3.py file,you only modify datacfg file path,save_dir path ,if you have pretrained model just set weights path.
```python
from models import *

if __name__ == "__main__":
    yolov3 = yolov3trainModel(yolov3cfg=r'models/yolov3.yaml', datacfg=r'data/myvoc.yaml',
                              hypcfg=r'data/hyps/hyp.scratch.yaml', save_dir=r'log/myvoc/train', weights='', epochs=200,
                              batchsize=8, imgsz=640, channel=3, nclass=20)
    yolov3.Update()
```
>yolov3 inference can run inferenceyolov3.py,you only modify weights path,and use opencv read image then get boundingbox results.
```python
from models import *

if __name__ == "__main__":
    yolov3 = yolov3inferenceModel(weights=r'log/train/exp2/weights/best.pt')
    image = cv2.imread(r'D:\challenge\project\PytorchYoloModel\data\testimages\peoples.png')
    yolov3.inference(image)
```
## Contact
* https://github.com/junqiangchen
* email: 1207173174@qq.com
* WeChat Public number: 最新医学影像技术
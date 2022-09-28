from models import *

if __name__ == "__main__":
    yolov3 = yolov3trainModel(yolov3cfg=r'models/yolov3.yaml', datacfg=r'data/myvoc.yaml',
                              hypcfg=r'data/hyps/hyp.scratch.yaml', save_dir=r'log/myvoc/train', weights='', epochs=200,
                              batchsize=8, imgsz=640, channel=3, nclass=20)
    yolov3.Update()

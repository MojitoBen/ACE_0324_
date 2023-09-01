# ACE_0324_
"Work progress, learning, and similar things."

**python resource**
https://github.com/FavioVazquez/ds-cheatsheets/tree/master/Python

**Requirements**
python 3.7 up     
darknet    
make sure your CUDA and cuDNN available    
Install yolov4    
Download:https://github.com/AlexeyAB/darknet.git    
Check Makefile:    
GPU=1    
CUDNN=1    
CUDNN_HALF=1    
OPENCV=1    
AVX=0    
OPENMP=0    
LIBSO=1    
ZED_CAMERA=0 # ZED SDK 3.0 and above    
ZED_CAMERA_v2_8=0 # ZED SDK 2.X    
DEBUG=1    
    
terminal, cd to darknet, and input:    
make    
    
if OK then try pretrain:    
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights    

./darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/person.jpg -i 0 -thresh 0.25    

DataBase、IP、Port、Storage    

from objdetection1 import *

import os
def main():
    # videoPath="test/vc1.mp4"
    videoPath=0

    configPath=os.path.join("models","ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath=os.path.join("models","frozen_inference_graph.pb")
    classesPath=os.path.join("models","coco.names")

    d=Detector(videoPath, configPath, modelPath, classesPath)

    d.onVideo()


if __name__=='__main__':
    main()

#import sys
import cv2 
#import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import imutils
from .yoloDet import YoloTRT

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.callback,
            1)
        self.bridge = CvBridge()

        self.model = YoloTRT(library="/home/minhman/ros2_yolov5_pkg/ros2_yolov5_pkg/yolov5/build/libmyplugins.so", engine="/home/minhman/ros2_yolov5_pkg/ros2_yolov5_pkg/yolov5/build/own.engine", conf=0.5, yolo_ver="v5")


    def callback(self, msg):
        # self.t1 = time.time()
        frame = self.bridge.imgmsg_to_cv2(msg, "8UC3")
        frame = imutils.resize(frame, width=600)
        detections, t = self.model.Inference(frame)
        for obj in detections:
            print("Result: ",obj['class'], obj['conf'], obj['box'])
        print("FPS: {} \n".format(1/t))
        cv2.imshow("Output", frame)
        cv2.waitKey(1)
        
def main(args=None):
    # check_requirements(exclude=('tensorboard', 'thop'))
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

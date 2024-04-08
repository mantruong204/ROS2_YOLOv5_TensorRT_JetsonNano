import cv2
#from geometry_msgs.msg import Twist
from rclpy.node import Node 
from cv_bridge import CvBridge 
from sensor_msgs.msg import Image 
import rclpy 

#from .Drive_Bot import Debugging

class Real_camera(Node):
    def __init__(self):

        super().__init__('real_camera_publisher')
        self.publisher = self.create_publisher(Image,'/camera/image_raw',10)
        timer_period = 1/30; self.timer = self.create_timer(timer_period, self.timer_callback)
        
        ### SOURCE OF THE REAL CAMERA HERE! ###
        self.cap_source = cv2.VideoCapture(0)								#Use logitech camera
        # self.cap_source = cv2.VideoCapture("/home/minhman/Downloads/scenes/video-test-280223.mp4")	#Use video
        # self.cap_source = cv2.VideoCapture("/home/bkflash/Downloads/video-test/full_no_crop.mp4")	#Use video
        #self.cap_source = cv2.VideoCapture("/home/bkflash/Downloads/video-test/2-duong-dut-net-detect-lane.mp4")
        
        # Set the video capture properties
        self.cap_source.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap_source.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        self.bridge   = CvBridge() # converting ros images to opencv data
        #self.Debug    = Debugging()
       

    def timer_callback(self):        
        """
        Callback function.
        This function gets called every 0.1 seconds.
        """
        #self.Debug.setDebugParameters()

        # Capture frame-by-frame
        # This method returns True/False as well
        # as the video frame.
        ret, frame = self.cap_source.read()
     
        
        if ret == True:
            # Publish the image.
            # The 'cv2_to_imgmsg' method converts an OpenCV
            # image to a ROS 2 image message
            self.publisher.publish(self.bridge.cv2_to_imgmsg(frame))
            
        # Display the message on the console
        self.get_logger().info('Publishing video frame')
        
 
def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)
    
    # Create the node
    image_publisher = Real_camera()
    
    # Spin the node so the callback function is called.
    rclpy.spin(image_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_publisher.destroy_node()
    
    # Shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
	main()

import rclpy
from rclpy.node import Node


from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic',10)

    def send_data(self,key):
        msg = String()
        msg.data = key
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    while True :
        key = input("entrer une string")
        minimal_publisher.send_data(key)


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
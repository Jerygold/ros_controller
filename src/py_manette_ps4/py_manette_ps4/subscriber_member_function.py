import rclpy
from rclpy.node import Node

from ps4_messages.msg import Manette

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Manette,
            'controller',
            self.listener,
            10)
        self.subscription # prevent unused variable warning
        

    def listener(self, msg):
        self.get_logger().info('%s / %s / %d' % (msg.is_accelerating, msg.is_desclerating, msg.joycon_value))
    
    



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
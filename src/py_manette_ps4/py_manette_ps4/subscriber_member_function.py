import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from std_msgs.msg import Bool
from std_msgs.msg import Int32

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription_accelerate = self.create_subscription(
            Bool,
            'accelerate',
            self.listener_accelerate,
            10)
        self.subscription_accelerate  # prevent unused variable warning
        
        self.subscription_descelerate = self.create_subscription(
            Bool,
            'descelerate',
            self.listener_descelerate,
            10
        )
        self.subscription_descelerate

        self.subscription_joycon =self.create_subscription(
            Int32,
            'joycon',
            self.listener_joycon,
            10
        )
        self.subscription_joycon

    def listener_accelerate(self, msg):
        self.get_logger().info('Acceleration "%s"' % msg.data)
    
    def listener_descelerate(self, msg):
        self.get_logger().info('Desceleration "%s"' % msg.data)
    
    def listener_joycon(self, msg):
        self.get_logger().info('Joycon "%s"' % msg.data)
    



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
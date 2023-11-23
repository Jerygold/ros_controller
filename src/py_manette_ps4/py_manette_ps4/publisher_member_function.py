import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Int32
import evdev


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_1 = self.create_publisher(Bool, 'accelerate', 10)
        self.publisher_2 = self.create_publisher(Bool, 'descelerate', 10)
        self.publisher_3 = self.create_publisher(Int32, 'joycon', 10)
        

    def send_accelerate(self,accelerate):
        msg = Bool()

        msg.data=accelerate
        self.publisher_1.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
    
    def send_descelerate(self,descelerate):
        msg = Bool()

        msg.data=descelerate
        self.publisher_2.publish(msg)
        self.get_logger().info('Publisging: "%s"'% msg.data)
    
    def send_joycon(self,entierJoycon):
        msg = Int32()

        msg.data=entierJoycon

        self.publisher_3.publish(msg)
        self.get_logger().info('Publishing "%s"'% msg.data)
        


def main(args=None):
    rclpy.init(args=args)
    


    minimal_publisher = MinimalPublisher()

    #rclpy.spin(minimal_publisher)
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    ps4_controller = None

    for device in devices:
        if "Wireless Controller" in device.name:
            ps4_controller = device
            break

    if ps4_controller is None:
        print("Manette de PS4 non trouvée.")
        exit()

    print("Manette de PS4 trouvée :", ps4_controller.name)


    for event in ps4_controller.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            key_event = evdev.categorize(event)
            if key_event.keystate == key_event.key_down:
                if key_event.keycode[0] == 'BTN_A' :
                    minimal_publisher.send_accelerate(True)
                elif key_event.keycode[0] == 'BTN_B':
                    minimal_publisher.send_accelerate(True)
            elif key_event.keystate == key_event.key_up:
                if key_event.keycode[0] == 'BTN_A' :
                    minimal_publisher.send_descelerate(False)
                elif key_event.keycode[0] == 'BTN_B':
                    minimal_publisher.send_descelerate(False)
                
        elif event.type == evdev.ecodes.EV_ABS:
            abs_event = evdev.categorize(event)
            if abs_event.event.code == evdev.ecodes.ABS_X:
                minimal_publisher.send_joycon(abs_event.event.value)
    
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
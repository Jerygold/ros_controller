import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import evdev


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        

    def send_data(self,entree):
        msg = String()
        msg.data = '%s' % entree
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        


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
                    minimal_publisher.send_data("ACCELERATE_TRUE")
                elif key_event.keycode[0] == 'BTN_B':
                    minimal_publisher.send_data("DESCELERATE_TRUE")
            elif key_event.keystate == key_event.key_up:
                if key_event.keycode[0] == 'BTN_A' :
                    minimal_publisher.send_data("ACCELERATE_FALSE")
                elif key_event.keycode[0] == 'BTN_B':
                    minimal_publisher.send_data("DESCELERATE_FALSE")
                
        elif event.type == evdev.ecodes.EV_ABS:
            abs_event = evdev.categorize(event)
            if abs_event.event.code == evdev.ecodes.ABS_X:
                minimal_publisher.send_data(abs_event.event.value)
    
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
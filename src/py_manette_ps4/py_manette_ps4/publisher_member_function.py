import rclpy
from rclpy.node import Node

from ps4_messages.msg import Manette

import evdev


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_1 = self.create_publisher(Manette, 'controller', 10)
        
        

    def send_data(self,accelerate,descelerate,joycon):
        msg = Manette()
        msg.is_accelerating = accelerate
        msg.is_desclerating = descelerate
        msg.joycon_value = joycon

        self.publisher_1.publish(msg)
        self.get_logger().info('Publishing: "%s" / "%s" / "%d"' % (msg.is_accelerating,msg.is_desclerating,msg.joycon_value))

    
        


def main(args=None):
    rclpy.init(args=args)
    
    accelerate =False
    descelerate =False
    joycon = 131


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
                    accelerate =True
                    minimal_publisher.send_data(accelerate,descelerate,joycon)
                elif key_event.keycode[0] == 'BTN_B':
                    descelerate = True
                    minimal_publisher.send_data(accelerate,descelerate,joycon)
            elif key_event.keystate == key_event.key_up:
                if key_event.keycode[0] == 'BTN_A' :
                    accelerate = False
                    minimal_publisher.send_data(accelerate,descelerate,joycon)
                elif key_event.keycode[0] == 'BTN_B':
                    descelerate = False
                    minimal_publisher.send_data(accelerate,descelerate,joycon)
                
        elif event.type == evdev.ecodes.EV_ABS:
            abs_event = evdev.categorize(event)
            if abs_event.event.code == evdev.ecodes.ABS_X:
                joycon = abs_event.event.value
                minimal_publisher.send_data(accelerate,descelerate,joycon)
    
    

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
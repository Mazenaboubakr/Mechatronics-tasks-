import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class EventLogger(Node):
    def __init__(self):
        super().__init__("event_logger")
        
        # Subscribers
        self.create_subscription(String, "security_event", self.event_callback, 10)
        self.create_subscription(String, "security_alert", self.alert_callback, 10)

        self.get_logger().info("Event Logger Node Started")

    def event_callback(self, msg):
        self.get_logger().info(f" EVENT: {msg.data}")

    def alert_callback(self, msg):
        self.get_logger().info(f" ALERT: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = EventLogger()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
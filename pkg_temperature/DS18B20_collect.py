import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from w1thermsensor import W1ThermSensor

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('DS18B20_collect')
        self.sensor = W1ThermSensor()

        self.publisher = self.create_publisher(Float64, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)

    def publish_temperature(self):
        temperature = self.sensor.get_temperature()
        msg = Float64()
        msg.data = temperature
        self.publisher.publish(msg)
        self.get_logger().info(f'Temperature: {temperature} Celsius')

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

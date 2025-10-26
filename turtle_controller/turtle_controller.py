import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class TurtleEight(Node):
    def __init__(self):
        super().__init__('turtle_eight_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.05, self.timer_callback)
        self.time = 0.0
        self.get_logger().info("Turtle figure-eight controller started!")

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0  # stała prędkość liniowa
        msg.angular.z = 1.5 * math.sin(0.5 * self.time)  # zmieniające się skręcanie
        self.publisher_.publish(msg)
        self.time += 0.05  # czas rośnie w każdej iteracji


def main(args=None):
    rclpy.init(args=args)
    node = TurtleEight()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

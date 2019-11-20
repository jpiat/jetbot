import time
import traitlets
import hoverboard_api
from traitlets.config.configurable import SingletonConfigurable


class Robot(SingletonConfigurable):

    # config
    self.serial_bus = b'/dev/ttyUSB0'
    self.serial_speed = 115200

    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.motor_driver = hoverboard_api.HoverboardAPI(self.serial_bus, self.serial_speed)

    def set_motors(self, left_speed, right_speed):
        self.motor_driver.sendSpeedData(left_speed, right_speed, 0, 0) #Not good for the last two args 

    def forward(self, speed=1.0, duration=None):
        self.motor_driver.sendSpeedData(speed, speed, 0, 0)

    def backward(self, speed=1.0):
        self.motor_driver.sendSpeedData(-speed, -speed, 0, 0)

    def left(self, speed=1.0):
        self.motor_driver.sendSpeedData(-speed, speed, 0, 0)

    def right(self, speed=1.0):
        self.motor_driver.sendSpeedData(speed, -speed, 0, 0)

    def stop(self):
        self.motor_driver.sendSpeedData(0, 0, 0, 0)

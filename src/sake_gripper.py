import sys
import time

import lcm

# TODO(sam.creasey) I have clearly messed up the bazel build
# declaration of libezgripper.  I do not know how to remove the
# redundant name.

from libezgripper.libezgripper import ezgripper_base
from libezgripper.libezgripper.lib_robotis import create_connection, Robotis_Servo

# TODO(sam.creasey) This is pretty kludgy, should probably fix in
# upstream drake.
import drake.lcmtypes
drake.__path__.append(drake.lcmtypes.__path__[0] + "/drake")

from drake import lcmt_schunk_wsg_command
from drake import lcmt_schunk_wsg_status

class SakeGripperDriver(object):
    def __init__(self):
        self.last_lcm_message = None
        self.lc = lcm.LCM()
        self.connection = create_connection(dev_name='/dev/ttyUSB0', baudrate=57600)
        self.gripper = ezgripper_base.Gripper(self.connection, 'gripper1', [1])
        self.gripper.calibrate()
        self.gripper.goto_position(100, 100) # open
        self.lc.subscribe("SCHUNK_WSG_COMMAND", self.handle_message)

    def handle_message(self, channel, msg_bytes):
        command = lcmt_schunk_wsg_command.lcmt_schunk_wsg_command.decode(msg_bytes)
        if self.last_lcm_message is not None:
            if (self.last_lcm_message.target_position_mm == command.target_position_mm and
                self.last_lcm_message.force == command.force):
                return
        self.last_lcm_message = command
        target = command.target_position_mm
        if target < 10:
            target = 0
        self.gripper.goto_position(target, command.force)

    def publish_status(self):
        status_msg = lcmt_schunk_wsg_status.lcmt_schunk_wsg_status()
        status_msg.actual_position_mm = self.gripper.get_position()
        status_msg.utime = time.time() * 1e6
        status_msg.actual_force = self.gripper.servos[0].read_load()
        # TODO(sam.creasey) fix the sign/scaling
        status_msg.actual_speed_mm_per_s = self.gripper.servos[0].read_present_speed()
        self.lc.publish("SCHUNK_WSG_STATUS", status_msg.encode());


    def step(self):
        self.lc.handle_timeout(1)
        self.publish_status()

    def wait_for_stop(self, servo):
        wait_start = time.time()
        last_position = 1000000 # read_encoder() cannot return more than 65536
        while True:
            current_position = servo.read_encoder()
            if current_position == last_position:
                break
            last_position = current_position
            time.sleep(0.1)
            print "publish"
            self.publish_status()

            if time.time() - wait_start > 5:
                break


def main():
    sake = SakeGripperDriver()
    ezgripper_base.wait_for_stop = sake.wait_for_stop
    while True:
        sake.step()


if __name__ == "__main__":
    main()

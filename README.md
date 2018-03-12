# sake-gripper-driver

This repository implements an LCM-based driver for the SAKE robotics
two-finger gripper.  It is based on libezgripper from
https://github.com/SAKErobotics/libezgripper
.

It requires that the `python-serial` package is installed.

The LCM communication is currently kludgy in that it uses the LCM
messages defined for the Schunk WSG from
https://github.com/RobotLocomotion/drake/tree/master/lcmtypes
.

To run:

    bazel build //...
    ./bazel-bin/src/sake_driver

# Green screen for Canoe freestyle timer

This software provides green screen for the canoe freestyle timer (github.com/proalvo/canoe-freestyle-timer) to bed used for live video streaming.

See the idea at Youtube: https://youtu.be/hxXWm2dkruE

## Requirements and installation

1. Raspberry PI + Raspbian OS
1. Disable screen saver
1. Istall Python 3
1. Provide fixed name for the USB port
1. Connect Canoe Freestyle timer to the Raspberry Pi's USB port
1. Copy the freestyle-timer-green-screen.py and run it

## How to disable screen saver

Original instrucation at https://www.geeks3d.com/hacklab/20160108/how-to-disable-the-blank-screen-on-raspberry-pi-raspbian/

You can disable the blank screen once with the following command line instructions:

$ sudo xset s off
$ sudo xset -dpms
$ sudo xset s noblank
 
xset s off disable the screen saver, xset -dpms disables the DPMS (Display Power Management Signaling) and xset s noblank tells to X server to not blank the video device.

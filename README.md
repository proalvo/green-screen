# Green screen for Canoe freestyle timer

This Python based software provides a green screen for the canoe freestyle timer (github.com/proalvo/canoe-freestyle-timer) to be used for live video streaming.

See the idea at Youtube: https://youtu.be/hxXWm2dkruE

Instructions are not very complete yet, I am working on those.

## Requirements and installation

1. Raspberry PI + Raspbian OS
1. Disable screen saver for GUI
1. Install Python 3
1. Provide fixed name for the USB port
1. Connect Canoe Freestyle timer to the Raspberry Pi's USB port
1. Copy the freestyle-timer-green-screen.py and run it

## How to disable screen saver

You need to disable screen saver to have green screen visible all the time.

Original instruction at https://www.geeks3d.com/hacklab/20160108/how-to-disable-the-blank-screen-on-raspberry-pi-raspbian/

You can disable the blank screen once with the following command line instructions:

```
$ sudo xset s off
$ sudo xset -dpms
$ sudo xset s noblank
``` 
xset s off disable the screen saver, xset -dpms disables the DPMS (Display Power Management Signaling) and xset s noblank tells to X server to not blank the video device.

## How to set fixed name for the USB port

Raspberry PI will set a new port name for the USB every time you restart the Arduino UNO. Luckily there is a methods to set fixed name. See instructions at:

https://www.domoticz.com/wiki/Assign_fixed_device_name_to_USB_port

Note that the python script is using the port name: /dev/ttyUSB_GREENSCREEN

# remote_snes_robot_controller
Remotely control your robot with USB SNES gamepad

result see on following video: https://www.youtube.com/embed/fkz6H1M2Crk


Here is guide how enable remote controll of your robot:

1. Enable Remote GPIO in your Pi (robot).

   How to do this please follow Ben Nutall's Gist
   https://gist.github.com/bennuttall/572789b0aa5fc2e7c05c7ada1bdc813e

2. Run sudo pigpiod daemon on Pi (robot).

3. Connect your gamepad to your computer (could be other Pi or other Linux, should work also on Windows but not tested)

   First plug the joystick into computer, this will be into a USB port from either the joysticks cable, or the wireless         receiver.
   You will now need to run the following to ensure the joystick drivers are installed:
   
   sudo apt-get -y install joystick
   
   Then you will want to run jstest as follows:
   
   jstest /dev/input/js0

4. Install python gpiozero, pygame libraries.

5. Download and update python script remote_snes_robot_controller.py with your remote Pi(robot) address.

6. Run script ...

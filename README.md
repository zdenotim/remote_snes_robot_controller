# remote_snes_robot_controller
Remotely control your robot with USB SNES gamepad

Here guide how enable remote controll of your robot:

1. Enable Remote GPIO in your Pi.

   How to do this please follow Ben Nutall's Gist
   https://gist.github.com/bennuttall/572789b0aa5fc2e7c05c7ada1bdc813e

2. Run sudo pigpiod daemon on Pi.

3. Connect your gamepad

   First plug the joystick into Raspberry Pi, this will be into a USB port from either the joysticks cable, or the wireless         receiver.
   You will now need to run the following to ensure the joystick drivers are installed:
   
   sudo apt-get -y install joystick
   
   Then you will want to run jstest as follows:
   
   jstest /dev/input/js0

3. Install python gpiozero, pygame libraries.

4. Download and update python script remote_snes_robot_controller.py with your remote Pi address.

   


<iframe width="560" height="315" src="https://www.youtube.com/embed/fkz6H1M2Crk" frameborder="0" allowfullscreen></iframe>

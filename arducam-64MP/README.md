## Driver Installation
https://www.arducam.com/downloads/64mp-autofocus-quad-camera-kit.pdf
```
wget -O install_pivariety_pkgs.sh https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver/releases/download/install_script/install_pivariety_pkgs.sh
chmod +x install_pivariety_pkgs.sh
./install_pivariety_pkgs.sh -p libcamera_dev
./install_pivariety_pkgs.sh -p libcamera_apps
./install_pivariety_pkgs.sh -p 64mp_pi_hawk_eye_kernel_driver
```
Open /boot/config.txt, under [all], add the following line:
```
dtoverlay=vc4-kms-v3d,cma-512
```
### Preview
libcamera-still -t 0 --viewfinder-width 2312 --viewfinder-height 1736

### Focus Control
```
git clone https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver.git cd Arducam-Pivariety-V4L2-Driver/focus
```
```
python3 FocuserExample.py -d /dev/v4l-subdev1 --focus-step 10
```
### Switch the Channel
channel 0: 
```
i2cset -y 10 0x24 0x24 0x02
```
channel 1: 
```
i2cset -y 10 0x24 0x24 0x12
```
channel 2: 
```
i2cset -y 10 0x24 0x24 0x22
```
channel 3: 
```
i2cset -y 10 0x24 0x24 0x32
```
double channel (single channel 0 and single channel 1)
```
i2cset -y 10 0x24 0x24 0x01
```
double channel (single channel 2 and single channel 3)
```
i2cset -y 10 0x24 0x24 0x11
```
four in one mode (Default)
```
i2cset -y 10 0x24 0x24 0x00
```

## Picamera2 Installation
https://www.arducam.com/docs/cameras-for-raspberry-pi/picamera2-with-arducam-v1-v2-hq-16mp-af-64mp-af-pivariety-cameras-guide/ 
```
sudo apt install -y python3-kms++
sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg
sudo pip3 install numpy --upgrade
sudo pip3 install picamera2==0.3.2
```
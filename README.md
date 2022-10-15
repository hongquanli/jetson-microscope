# jetson-microscope
## Install Argus
[reference](https://developer.ridgerun.com/wiki/index.php?title=Xavier/Video_Capture_and_Display/Software_Support/Libargus)
`argus_camera` is a graphical user interface that you can use to snap images and make recordings. To install, open a terminal, then
```
sudo apt-get update
sudo apt-get install build-essential pkg-config libx11-dev libgtk-3-dev libjpeg-dev libegl1-mesa-dev libgles2-mesa-dev libgstreamer1.0-dev
```
```
cp -rf /usr/src/jetson_multimedia_api ~/
cd ~/jetson_multimedia_api/argus
mkdir build
cd build
cmake ..
make
sudo make install
```

## Install ArduCam IMX477
[Hardware Setup Instructions](https://www.arducam.com/docs/camera-for-jetson-nano/native-jetson-cameras-imx219-imx477/imx477/)
## Install camera driver for ArduCam IMX477
Open a terminal, then
```
cd ~
wget https://github.com/ArduCAM/MIPI_Camera/releases/download/v0.0.3/install_full.sh
chmod +x install_full.sh
./install_full.sh -m imx477
```

## Using argus_camera
Suggestions:
- fix the exposure time e.g. (10000000 ns - 10000000 ns)so that auto-exposure does not adjust the exposure time
- fix the gain e.g. (1.5 - 1.5). Use lower gain for higher full well capacity to get higher SNR. Use higher gain for low light/short exposure time.
- fix the ISP digital gain (1 - 1)

# jetson-microscope
## ArduCam IMX477
[Hardware Setup Instructions](https://www.arducam.com/docs/camera-for-jetson-nano/native-jetson-cameras-imx219-imx477/imx477/)
## Install camera driver for ArduCam IMX477
```
cd ~
wget https://github.com/ArduCAM/MIPI_Camera/releases/download/v0.0.3/install_full.sh
chmod +x install_full.sh
./install_full.sh -m imx477
```
## Install Argus
[reference](https://developer.ridgerun.com/wiki/index.php?title=Xavier/Video_Capture_and_Display/Software_Support/Libargus)
```
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

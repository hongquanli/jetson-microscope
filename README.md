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
```
cp -rf /usr/src/jetson_multimedia_api ~/
cd ~/jetson_multimedia_api/argus
mkdir build
cd build
cmake ..
make
make install
```

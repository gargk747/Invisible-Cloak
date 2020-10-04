# Invisible-Cloak

### First run background.py to get the background image(press 'q' to capture background)
 
 
 
 ### Then run invisible_cloak.py to see the magic.
 
 # Working
 
 This technique is opposite to the Green Screening. In green screening, we remove background but here we will remove the foreground frame.
 1. Capture and store the background frame
 2. Detect the defined color using color detection and segmentation algorithm.
 3. Segment out the defined colored part by generating a mask.

# Requirements

 1. OpenCV will be used for image processing part i.e. to start the camera, read each frame in code, color detection, color masking, and streaming final result
 
 2.Numpy will be used to deal with arrays as images in python are a series of Numpy array

![alt text](https://github.com/sdas969/Invisible-Cloak/raw/master/1_zAHne2Liz8RpCfTgqbCwYw.gif)

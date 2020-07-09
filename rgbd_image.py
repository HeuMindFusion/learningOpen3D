import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# monkey patches visualization and provides helpers to load geometries
sys.path.append('..')

print("Read Redwood dataset")
color_raw = o3d.io.read_image("../../test_data/RGBD/color/00000.jpg")
depth_raw = o3d.io.read_image("../../test_data/RGBD/depth/00000.png")
help( o3d.geometry.RGBDImage)
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_raw, depth_raw)

print(rgbd_image)

plt.subplot(1, 2, 1)
plt.title('Redwood grayscale image')
plt.imshow(color_raw)
plt.subplot(1, 2, 2)
plt.title('Redwood depth image')
plt.imshow(depth_raw)
plt.show()
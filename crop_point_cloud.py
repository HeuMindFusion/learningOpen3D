import open3d as o3d   #导入open3d
import numpy as np


##裁剪点云
print("Load a polygon volume and use it to crop the original point cloud")
pcd = o3d.io.read_point_cloud("./test_data/fragment.ply")
vol = o3d.visualization.read_selection_polygon_volume("./test_data/Crop/cropped.json")
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair])

##上色
##paint_uniform_color给所有的点上一个统一的颜色，颜色是在RGB空间得[0，1]范围内得值。
print("Paint chair")
chair.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([chair])


##包围框
##点云几何类型和其他类型一样，也有包围框。当前，open3d实现了两个包围框接口，同时他们也可以用来裁剪几何图形。
aabb = chair.get_axis_aligned_bounding_box()
aabb.color = (1,0,0)
obb = chair.get_oriented_bounding_box()
obb.color = (0,1,0)
o3d.visualization.draw_geometries([chair, aabb, obb])
import open3d as o3d   #导入open3d
import numpy as np
import matplotlib.pyplot as plt

pcd = o3d.io.read_point_cloud("./test_data/fragment.pcd")

print("Convert mesh to a point cloud and estimate dimensions")
#pcd = o3dtut.get_armadillo_mesh().sample_points_poisson_disk(5000)
diameter = np.linalg.norm(np.asarray(pcd.get_max_bound()) - np.asarray(pcd.get_min_bound()))
o3d.visualization.draw_geometries([pcd])

print("Define parameters used for hidden_point_removal")
camera = [0, 0, diameter]
radius = diameter * 100


print("Get all points that are visible from given view point")
_, pt_map = pcd.hidden_point_removal(camera, radius)


print("Visualize result")
pcd = pcd.select_by_index(pt_map)
o3d.visualization.draw_geometries([pcd])
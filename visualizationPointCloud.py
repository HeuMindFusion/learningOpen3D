import open3d as o3d   #导入open3d
import numpy as np

#读取点云数据并将其可视化。
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("./test_data/fragment.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])


# 体素降采样通过使用规则提速网格从输入点云创造一致化降采样点云。这通常在点云处理任务的预处理步骤，这个算法分为两步：
# 把点云装进体素网格
# 把每个被占据的体素中的点做平均，取一个精确的点。
print("Downsample the point cloud with a voxel of 0.05")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
o3d.visualization.draw_geometries([downpcd])

#点云的基本操作还包括定点法线估计。按 n 查看点云法线。使用 - 和 + 可以缩放法线长度

print("Recompute the normal of the downsampled point cloud")
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd], 
                                  point_show_normal=True)


#通过downpcd的normals参数可以检索估计的点的法线。

print("Print a normal vector of the 0th point")
print(downpcd.normals[0])

print(np.asarray(downpcd.normals)[:10,:])
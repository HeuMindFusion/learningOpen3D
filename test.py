import open3d as o3d   #导入open3d
## 读取点云
pcd = o3d.io.read_point_cloud("./test_data/ICP/cloud_bin_0.pcd")
print(pcd)

## 可以打印open3d模块文件
#help(o3d)

## help(open3d.PointCloud)可以用来打印PointCloud类的描述。
#help(o3d.geometry.PointCloud)

#help(open3d.io.read_point_cloud)提供了read_point_cloud函数的描述，主要包括输入参数和返回类型。
#help(o3d.io.read_point_cloud)

##基本几何图形的读取和写入，点云（Point Cloud）通过下面的代码读写点云
print("Testing IO for point cloud ...")
pcd = o3d.io.read_point_cloud("./test_data/fragment.pcd")
print(pcd)
o3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)
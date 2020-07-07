import open3d as o3d   #导入open3d
import numpy as np
import matplotlib.pyplot as plt
import copy


mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_r = copy.deepcopy(mesh)
R = mesh.get_rotation_matrix_from_xyz((np.pi/2,0,np.pi/4))
mesh_r.rotate(R, center=(0,0,0))
o3d.visualization.draw_geometries([mesh, mesh_r])


mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_r = copy.deepcopy(mesh).translate((2,0,0))
mesh_r.rotate(mesh.get_rotation_matrix_from_xyz((np.pi/2,0,np.pi/4)), center=(0,0,0))
o3d.visualization.draw_geometries([mesh, mesh_r])


##Open3d里面的顶点和点可以应用scale进行缩放，v_s=s⋅v。
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_s = copy.deepcopy(mesh).translate((2,0,0))
mesh_s.scale(0.5, center=mesh_s.get_center())
o3d.visualization.draw_geometries([mesh, mesh_s])

##scale算法默认第二个参数center也是True。如果设置为False，对象在缩放前没有居中，这样就可以移动对象的中心。
mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_s = copy.deepcopy(mesh).translate((2,1,0))
mesh_s.scale(0.5, center=(0,0,0))
o3d.visualization.draw_geometries([mesh, mesh_s])

# 通用的变换
# Open3d还支持通过通用的4×44×4的矩阵进行变换。接口为transform。

mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
T = np.eye(4)
T[:3,:3] = mesh.get_rotation_matrix_from_xyz((0,np.pi/3, np.pi/2))
T[0,3] = 1
T[1,3] = 1.3
print(T)
mesh_t = copy.deepcopy(mesh).transform(T)
o3d.visualization.draw_geometries([mesh, mesh_t])
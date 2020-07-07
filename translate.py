import open3d as o3d   #导入open3d
import numpy as np
import matplotlib.pyplot as plt
import copy

# 这里我们展示的第一个算法是平移。
# 平移算法就是通过单个三维向量 ttt 来平移所有点/顶点，vt=v+tv_{t} = v + tvt=v+t。
# 下面的代码展示了网格分别在x方向和y方向平移一次的结果。


mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_tx = copy.deepcopy(mesh).translate((1.3,0,0))
mesh_ty = copy.deepcopy(mesh).translate((0,1.3,0))
print(f'Center of mesh: {mesh.get_center()}')
print(f'Center of mesh tx: {mesh_tx.get_center()}')
print(f'Center of mesh ty: {mesh_ty.get_center()}')
o3d.visualization.draw_geometries([mesh, mesh_tx, mesh_ty])


mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh_mv = copy.deepcopy(mesh).translate((2,2,2), relative=False)
print(f'Center of mesh: {mesh.get_center()}')
print(f'Center of translated mesh: {mesh_mv.get_center()}')
o3d.visualization.draw_geometries([mesh, mesh_mv])
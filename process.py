import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt


def convert_las_to_ply(las_file, ply_file):
    # print(las_file)
    # print(ply_file)
    # print("convert_las_to_ply")

    # อ่านไฟล์ .las

    # บันทึกเป็นไฟล์ .ply
    pcd = o3d.io.read_point_cloud(las_file)
    o3d.io.write_point_cloud(ply_file, pcd)

    points = np.asarray(pcd.points)
    variance_values = np.var(points, axis=0)
    mean_values = np.mean(points, axis=0)

    num_dimensions = points.shape[1]
    fig, axs = plt.subplots(num_dimensions, figsize=(8, 2 * num_dimensions))
    axis = ['X', 'Y', 'Z']
    fig.suptitle("Khodhin 5", fontsize=16)

    for dim in range(num_dimensions):
        axs[dim].hist(points[:, dim], bins=50, color='blue', alpha=0.7)
        axs[dim].set_title(
            f"Dimension {axis[dim]} - Variance: {variance_values[dim]:.4f}, Mean: {mean_values[dim]:.4f}")

    plt.tight_layout()
    # use plt to convert to picture and return the picture
    path_store = 'store/'
    final_path = path_store + 'histogram.png'
    plt.savefig(final_path)
    return final_path

convert_las_to_ply("Khodhin_5.las", "Khodhin_5.ply")

# # อ่าน point cloud จากไฟล์ .ply
# pcd = o3d.io.read_point_cloud("Khodhin_5.ply")
# points = np.asarray(pcd.points)

# # คำนวณค่าความแปรปรวนและค่าเฉลี่ยของทุก dimension
# variance_values = np.var(points, axis=0)
# mean_values = np.mean(points, axis=0)

# # พล็อต histogram และแสดงค่า variance ในแต่ละ dimension
# num_dimensions = points.shape[1]
# fig, axs = plt.subplots(num_dimensions, figsize=(8, 2 * num_dimensions))
# axis = ['X', 'Y', 'Z']

# # กำหนดชื่อของ Figure เป็น "Segment1"
# fig.suptitle("Khodhin 5", fontsize=16)

# for dim in range(num_dimensions):
#     axs[dim].hist(points[:, dim], bins=50, color='blue', alpha=0.7)
#     axs[dim].set_title(f"Dimension {axis[dim]} - Variance: {variance_values[dim]:.4f}, Mean: {mean_values[dim]:.4f}")

# plt.show()
# plt.tight_layout()

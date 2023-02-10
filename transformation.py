import numpy as np
from modules.vis import plot_pointcloud
import itertools


def transform(point:np.array, trans:list[float]=[0, 0, 0], scale:list[float]=[0, 0, 0], rot_angle:list[float]=[0, 0, 0]):
    
    ## translation
    trans_mat = np.eye(4)
    trans_mat[:3, -1] = trans
    
    ## scale matrix 
    scale_mat = np.eye(4)
    scale_mat[:3, :3] = np.diag(scale)
    
    ## rotation 
    rot_mat = np.eye(4)
    rot_mat = np.tile(rot_mat, (3, 1, 1))
    
    rot_rad = [angle * np.pi / 180 for angle in rot_angle] 
    
    for i, rad in enumerate(rot_rad):
        indices = [idx for idx in range(3) if idx != i]
        positions = list(itertools.product(indices, indices))

        rot_matrix = np.array([[np.cos(rad), -np.sin(rad)], 
                               [np.sin(rad), np.cos(rad)]])

        for x, y in positions:
            x_ = x 
            y_ = y
            if x_ > i: 
                x_ -= 1 
            if y > i: 
                y_ -= 1 
            
            rot_mat[i, x, y] = rot_matrix[x_, y_]
    
    input = np.hstack([point, np.ones(len(point_set)).reshape(-1, 1)])
    input = np.transpose(input)
    
    ## translation 
    transformed  = trans_mat @ input 
    
    ## scaling 
    transformed = scale_mat @ transformed
    
    ## rotation 
    for i in range(3):
        transformed = rot_mat[i] @ transformed
    
    return np.transpose(transformed[:3, :])

if __name__=="__main__": 
    
    obj_file = './data/shapenet/02691156/1021a0914a7207aff927ed529ad90a11.pts'
    
    translation = [100.0, 5.0, 10.0]
    scale = [1, 2, 0.5]
    rotation = [90.0, 0.0, 0.0]

    point_set = np.loadtxt(obj_file).astype(np.float32)
    plot_pointcloud(point_set)
    
    transformed = transform(point_set, trans = translation, scale = scale, rot_angle = rotation)
    plot_pointcloud(transformed)
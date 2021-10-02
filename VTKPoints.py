# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:18:05 2021

@author: Zikantika
"""

import numpy as np
from mayavi import mlab
import vtk
from scipy.spatial import Delaunay

def stlcreator(pm,filepath):
   # """ generates stl file """ based on point cloud data
         # pm is a 3D point cloud array
    x = pm[:, 0]
    y = pm[:, 1]
    z = pm[:, 2]
    xy = np.column_stack((x, y))
    Tri = Delaunay(xy) # Divide the plane triangle mesh
    Element = tri.simplices # The index number of the point contained in each triangle mesh
    Surface = mlab.pipeline.triangular_mesh_source(x, y, z, element) #Create a triangular surface
    Surface_vtk = surface.outputs[0]._vtk_obj # Generate vtk file
    stlWriter = vtk.vtkSTLWriter() # stl generator
    stlWriter.SetFileName(filepath) # set file path
    stlWriter.SetInputConnection(surface_vtk.GetOutputPort()) # Set the vtk interface of stlWriter
    stlWriter.Write() # save the surface to stl
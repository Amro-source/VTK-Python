# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:12:14 2021

@author: Zikantika
"""

import vtk

sphere = vtk.vtkSphereSource()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

window.Render()


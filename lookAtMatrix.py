#zaxis = normal(At - Eye)
#xaxis = normal(cross(Up, zaxis))
#yaxis = cross(zaxis, xaxis)
#
# xaxis.x           yaxis.x           zaxis.x          0
# xaxis.y           yaxis.y           zaxis.y          0
# xaxis.z           yaxis.z           zaxis.z          0
#-dot(xaxis, eye)  -dot(yaxis, eye)  -dot(zaxis, eye)  l

#dot(xaxis,-eye)  dot(yaxis,-eye)  dot(zaxis,-eye)  1 

import bpy
from mathutils import *
import mathutils as m
import math
from copy import deepcopy


objs =  bpy.context.selected_objects


at_ob = bpy.data.objects['Empty']

for ob in objs:
    if ob.type != 'MESH':
        break
    
    At = at_ob.location
    Eye = ob.location
    
    Pos = deepcopy(Eye)
    
    Up = Vector (( 1,0,0))
    
    zaxis = At - Eye
    zaxis.normalize()
    
    
    xaxis = Vector.cross(Up, zaxis)
    xaxis.normalize()
    
    yaxis = Vector.cross(zaxis, xaxis)
    
    lookMatrix = m.Matrix()
    
    lookMatrix[0] = Vector(( xaxis.x, yaxis.x, zaxis.x, 0 ))
    lookMatrix[1] = Vector(( xaxis.y, yaxis.y, zaxis.y, 0 ))
    lookMatrix[2] = Vector(( xaxis.z, yaxis.z, zaxis.z, 0 ))
    lookMatrix[3] = Vector(( Vector.dot(xaxis, -Eye) , Vector.dot(yaxis, -Eye), Vector.dot(zaxis, -Eye), 1 ))
    
    
    rot = Matrix.Rotation(math.radians(0), 4, 'Y' )
    
    ob.matrix_world = lookMatrix * rot
    ob.location = Pos



print(lookMatrix)

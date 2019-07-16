import bpy
import os 
import glob 
from bpy import context
import mathutils
import numpy as np 
import random 
from math import radians

bpy.ops.object.select_all(action='SELECT') 
bpy.ops.object.delete() # delete all 


scn=bpy.context.scene

bpy.context.scene.mblab_use_lamps = False
bpy.context.scene.mblab_use_eevee = True
bpy.context.scene.mblab_use_cycles = False# oh boy
#bpy.context.scene.mblab_use_muscle = True
bpy.context.scene.mblab_use_ik = True

ethnicity='f_af01'
bpy.context.scene.mblab_character_name = ethnicity
bpy.ops.mbast.init_character() # create character

bpy.context.object.skin_veins = 0
bpy.context.object.skin_bump = 0.25
bpy.context.object.skin_oil = 0.5
if "as01" in ethnicity:                
    bpy.context.object.skin_complexion = random.uniform(0,0.3)
    bpy.context.object.skin_saturation = random.uniform(0.75,0.95)
    bpy.context.object.skin_sss = random.uniform(0,0.4)
    bpy.context.object.skin_value = random.uniform(0.7,1)

if "ca01" in ethnicity:
    bpy.context.object.skin_complexion = random.uniform(0,0.25)
    bpy.context.object.skin_saturation = random.uniform(0.75,0.9)
    bpy.context.object.skin_sss = random.uniform(0,0.3)
    bpy.context.object.skin_value = random.uniform(0.85,1.0)

if "af01" in ethnicity:
    bpy.context.object.skin_complexion = random.uniform(0.4,0.8)
    bpy.context.object.skin_saturation = random.uniform(0.9,1.0)
    bpy.context.object.skin_sss = random.uniform(0.5,1)
    bpy.context.object.skin_value = random.uniform(0.6,1)

bpy.context.scene.mblab_final_prefix = "A"
bpy.ops.mbast.finalize_character()


#########################################POSING##############################################################
bpy.context.object.pose.bones["IK_control_hd"].location= [random.uniform(-1,1),random.uniform(-0.5,0.8),random.uniform(-1,1)]  #head
bro="IK_control_"
arr= [bro+'a_',bro+'ft_',bro+'ebw_',bro+'hl_', bro+'h_',bro+'fg06_']
side = ['R','L']
x1=[-1,-1,-1,-0.5,-0.6,-1]
x2=[0.3,0.1,1,0.5,0.8,1]      
y1=[-1,-0.8,-1,-0.5,-0.8,-1]
y2=[0.5,0.6,1,0.5,0.8,1]
z1=[-0.1,0,-1,-0.5,-0.9,-1]
z2=[1,0.5,1,0.5,0.9,1]
for i in range (3): #translation
    bpy.context.object.pose.bones[arr[i]+'R'].location=[random.uniform(x1[i],x2[i]),random.uniform(y1[i],y2[i]),random.uniform(z1[i],z2[i])]
    bpy.context.object.pose.bones[arr[i]+'L'].location=[-random.uniform(x1[i],x2[i]),random.uniform(y1[i],y2[i]),random.uniform(z1[i],z2[i])]
for i in range (3,6): #rotation
    bpy.context.object.pose.bones[arr[i]+'R'].rotation_mode='XYZ'
    bpy.context.object.pose.bones[arr[i]+'R'].rotation_euler=[random.uniform(x1[i],x2[i]),random.uniform(y1[i],y2[i]),random.uniform(z1[i],z2[i])]
    bpy.context.object.pose.bones[arr[i]+'L'].rotation_mode='XYZ'
    bpy.context.object.pose.bones[arr[i]+'L'].rotation_euler=[random.uniform(x1[i],x2[i]),random.uniform(y1[i],y2[i]),-random.uniform(z1[i],z2[i])]
bpy.ops.object.mode_set(mode='OBJECT')

######################################### clothes ###########################################
objects=bpy.data.objects
a=bpy.data.objects['A_armature']
 ################################## ROTATE PERSON RANDOMLY################
a.rotation_euler= (random.uniform(radians(-90),radians(90)),0,0) # rotate person

#bpy.data.objects['A_armature'].select_set(True) 
arm=bpy.data.objects[0]  
locaa =arm.matrix_world @ arm.pose.bones[108].matrix @ arm.pose.bones[108].location # getting global cordinates for the head
print(locaa)

''' 
This script was adapted from a couple of users on StackExchange:
    Mike - https://blender.stackexchange.com/users/85311/mike
    Johannes Riegraf - https://blender.stackexchange.com/users/51654/johannes-riegraf
Original thread:
    https://blender.stackexchange.com/questions/160739/loop-cut-and-slide-using-python-not-working/
'''
    

import bpy

# new_type is the area we need to switch to for our code to work
new_type = 'VIEW_3D'
scene = bpy.context.scene

# This stores our current area so we can return to it
old_type = bpy.context.area.type
# Now we switch to the new area type
bpy.context.area.type = new_type

# This function, combined with the override below, will force Blender to
# return the area that we want our code to run in, avoiding context errors
def recontext(return_area = False):
    for area in bpy.context.window.screen.areas:
        if area.type == new_type:
            space = area.spaces[0]
            for region in area.regions:
                if region.type == 'WINDOW':
                    if return_area: return region, space, area
                    return region, space
    return None, None

region, space, area = recontext(True)

override = {'scene': scene,'region': region, 'area': area, 'space': space}

# Your code goes here
bpy.ops.object.editmode_toggle()

bpy.ops.mesh.loopcut(
    override,
    number_cuts=1, 
    smoothness=0, 
    falloff='INVERSE_SQUARE', 
    object_index=0, 
    edge_index=0,
    mesh_select_mode_init=(True, False, False)
)

bpy.ops.object.editmode_toggle()
# Your code ends

# This line returns us to our original area type
bpy.context.area.type = old_type

import bpy

'''Add and Edit Modifiers'''

object = bpy.context.object

bpy.ops.object.modifier_add(type='SUBSURF')

subsurf = object.modifiers['Subdivision']
subsurf.subdivision_type = 'CATMULL_CLARK'
subsurf.levels = 2
subsurf.render_levels = 4

bpy.ops.object.modifier_add(type='ARRAY')

array = object.modifiers['Array']
array.count = 4
array.relative_offset_displace[0] = 0
array.relative_offset_displace[1] = 1
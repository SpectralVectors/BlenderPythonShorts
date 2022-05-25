import bpy

'''Edit Objects (Advanced)'''

object = bpy.context.object

bpy.ops.object.editmode_toggle()

bpy.ops.mesh.inset(thickness=0.3)

bpy.ops.mesh.bevel(offset=0.1)

bpy.ops.mesh.extrude_region_move(
                                MESH_OT_extrude_region={}, 
                                TRANSFORM_OT_translate={"value":(-1, 0, 0)}
                                )

bpy.ops.mesh.subdivide()


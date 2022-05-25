import bpy

'''Edit an Object (Basic)'''

object = bpy.context.object
object.select_set(True)

# Location

# Set Location (Absolute)
object.location = (0,1,0)

# Set Location (Add to Current)
object.delta_location = (0,1,0)

# Rotation

# Set Rotation (Absolute)
object.rotation_euler = (1.5708,0,0)

# Set Rotation (Add to Current)
object.delta_rotation_euler = (1.5708,0,0)

# Scale

# Set Scale (Absolute)
object.scale = (2,1,1)

# Set Scale (Add to Current)
object.delta_scale = (2,1,1)
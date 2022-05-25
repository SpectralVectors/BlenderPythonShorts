import bpy

'''Create and Assign a Material'''

# Create a Material
material = bpy.data.materials.new(name='MyMaterial')
material.use_nodes = True

# Assign the New Material to the Active Object
bpy.context.object.data.materials.append(material)

# Assign an Existing Material by Name
bpy.context.object.data.materials.append(bpy.data.materials['Material'])

# Reorder the Material Stack
# Select the material you want to move
# 0 is the first, 1 is the second etc
bpy.context.object.active_material_index = 0

# Move the Material through the Stack
bpy.ops.object.material_slot_move(direction='UP')
bpy.ops.object.material_slot_move(direction='DOWN')

# Add or Remove Material Slots
bpy.ops.object.material_slot_add()
bpy.ops.object.material_slot_remove()
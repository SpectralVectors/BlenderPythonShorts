import bpy

'''Select or Deselect the Active Object'''
# Select
bpy.context.object.select_set(True)

# Deselect
bpy.context.object.select_set(False)


'''Select or Deselect an Object by Name'''
# Select
bpy.data.objects['Cube'].select_set(True)

# Deselect
bpy.data.objects['Cube'].select_set(False)


'''Select or Deselect a Group of Objects'''
# Create the list of objects to select or deselect
cube = bpy.data.objects['Cube']
camera = bpy.data.objects['Camera']
light = bpy.data.objects['Light']

objects =  (cube,
            camera,
            light)

# Select
for object in objects:
    object.select_set(True)
    
# Deselect
for object in objects:
    object.select_set(False)
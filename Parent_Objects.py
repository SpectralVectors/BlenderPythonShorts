import bpy

'''Parent an Object'''

cube = bpy.data.objects['Cube']
camera = bpy.data.objects['Camera']

cube.parent = camera
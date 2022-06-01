# BlenderPythonShorts
A Collection of basic scripts to help beginners with Blender Python - bpy

## Table of Contents
### How to
[Add an Object](#how-to-add-an-object)

[Select Deselect Objects](#how-to-select-or-deselect-an-object)

## How to Add an Object
```python
import bpy

'''Add an Object'''

# Add Objects - Default

# Cube
bpy.ops.mesh.primitive_cube_add()

# UV Sphere
bpy.ops.mesh.primitive_uv_sphere_add()

# Empty 
bpy.ops.object.empty_add()

# Light
bpy.ops.object.light_add()

# Camera
bpy.ops.object.camera_add()

# Curve
bpy.ops.curve.primitive_bezier_curve_add()

# Text
bpy.ops.object.text_add()

# Armature
bpy.ops.object.armature_add()

# Grease Pencil Stroke
bpy.ops.object.gpencil_add()

# Add Objects - Advanced

# Cube
bpy.ops.mesh.primitive_cube_add(size=2, 
                                enter_editmode=False, 
                                align='WORLD', 
                                location=(0, 0, 0), 
                                scale=(1, 1, 1)
                                )

# UV Sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, 
                                     enter_editmode=False, 
                                     align='WORLD', 
                                     location=(0, 0, 0), 
                                     scale=(1, 1, 1))

# Empty
bpy.ops.object.empty_add(type='PLAIN_AXES', 
                         align='WORLD', 
                         location=(0, 0, 0), 
                         scale=(1, 1, 1))

# Light
bpy.ops.object.light_add(type='POINT', 
                         radius=1, 
                         align='WORLD', 
                         location=(0, 0, 0), 
                         scale=(1, 1, 1)
                         )

# Camera
bpy.ops.object.camera_add(enter_editmode=False, 
                          align='VIEW', 
                          location=(0, 0, 0), 
                          rotation=(1.10871, 0.0132652, 1.14827), 
                          scale=(1, 1, 1)
                          )

# Curve
bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, 
                                         align='WORLD', 
                                         location=(0, 0, 0), 
                                         scale=(1, 1, 1)
                                         )

# Text
bpy.ops.object.text_add(enter_editmode=False, 
                        align='WORLD', 
                        location=(0, 0, 0), 
                        scale=(1, 1, 1)
                        )

# Armature
bpy.ops.object.armature_add(enter_editmode=False, 
                            align='WORLD', 
                            location=(0, 0, 0), 
                            scale=(1, 1, 1)
                            )

# Grease Pencil Stroke
bpy.ops.object.gpencil_add(align='WORLD', 
                           location=(0, 0, 0), 
                           scale=(1, 1, 1), 
                           type='STROKE'
                           )
```

## How to Select or Deselect an Object
```python
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
```

## How to Delete Objects
```python
import bpy

'''Delete the Active Object'''

# First you must ensure only the objects
# you want to delete are selected

# Delete
bpy.ops.object.delete()
```

## How to Edit Objects (Basic)
```python
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
```

## How to Select a Vertex, Edge or Face
```python
import bpy

'''Select a Vertex, Edge or Face'''

object = bpy.context.object
data = object.data

# First Deselect anything that may be selected
bpy.ops.mesh.select_all(action='DESELECT')

# Switch Edit/Object Mode
bpy.ops.object.editmode_toggle()

# Select Vertex
data.vertices[2].select = True

# Select Edge
data.edges[2].select = True

# Select Face
data.polygons[2].select = True

# Switch Edit/Object Mode
bpy.ops.object.editmode_toggle()
```

## How to Edit Objects (Complex)
```python
import bpy

'''Edit Objects (Complex)'''

object = bpy.context.object

bpy.ops.object.editmode_toggle()

bpy.ops.mesh.inset(thickness=0.3)

bpy.ops.mesh.bevel(offset=0.1)

bpy.ops.mesh.extrude_region_move(
                                MESH_OT_extrude_region={}, 
                                TRANSFORM_OT_translate={"value":(-1, 0, 0)}
                                )

bpy.ops.mesh.subdivide()
```

## How to Create and Assign a Material
```python
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
```

## How to Create and Edit a Shader Node Tree
```python
# Create and Edit a Shader Node Tree

import bpy

# Create a Material to hold the Node Tree
material = bpy.data.materials.new(name='MyCoolMaterial')
material.use_nodes = True
material.node_tree.nodes.clear()

# Create the Node Tree
nodes = material.node_tree.nodes

# Add a Material Output, then any other nodes you want
output = nodes.new(type='ShaderNodeOutputMaterial')

# Add a Principled BSDF Shader, and adjust some values
bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
# Set the Base Color to Green
bsdf.inputs[0].default_value = (0, 1, 0, 1)
# Set the Roughness to 1
bsdf.inputs[9].default_value = 1
# Move the node 100 pixels to the left, so it does not overlap the Material Output node
bsdf.location[0] += -100

# Add a Noise Texture Node
noise = nodes.new(type='ShaderNodeTexNoise')
# Increase the Scale to 7
noise.inputs[2].default_value = 7
# Move it 200 pixels to the left so it does not overlap the Output or BSDF nodes
noise.location[0] += -200

# Now to connect the nodes
links = material.node_tree.links
# Create a connection between the first output of the Principled BSDF and the first input of the Material Output
links.new(bsdf.outputs[0], output.inputs[0])
# Create a connection between the first output of the Noise node and the Metallic input of the Principled BSDF
links.new(noise.outputs[0], bsdf.inputs[6])

# Now we add the material to the active object, otherwise it will be created but not used
bpy.context.object.data.materials.append(material)
```

## How to Activate / Deactivate Addons
```python
import bpy

'''Activate or Deactivate an Addon'''

# Activate
bpy.ops.preferences.addon_enable(module="node_arrange")

# Deactivate
bpy.ops.preferences.addon_disable(module="node_arrange")
```

## How to Add and Edit Modifiers
```python
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
```

## How to Parent Objects
```python
import bpy

'''Parent an Object'''

cube = bpy.data.objects['Cube']
camera = bpy.data.objects['Camera']

cube.parent = camera
```

## How to Install Python Libraries to Blender's Python
```python
# You MUST run Blender as Administrator for this script to work
# Right Click on Blender.exe, and choose Run > As Administrator
# Otherwise you will get a Permission Error and the script will fail

import bpy, subprocess, sys

versionnumber = str(bpy.data.version)
versionstring = versionnumber.replace(',','.').replace(' ','').replace('(','')
version = versionstring.rstrip(versionstring[-3:])

packages = ["shapely", "Equation"]

subprocess.check_call([
    sys.executable, 
    "-m", "ensurepip"])

subprocess.check_call([
    sys.executable, 
    "-m", "pip", "install", "--upgrade", "pip"])

for package in packages:
    subprocess.check_call([
        sys.executable, 
        "-m", "pip", "install",
        "--target=C:\\Program Files\\Blender Foundation\\Blender " + version + "\\" + version + "\\python\\lib", 
        package])
```

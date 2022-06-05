# BlenderPythonShorts
A Collection of basic scripts to help beginners with Blender Python - bpy

## Table of Contents
### How to
- [Add an Object](#how-to-add-an-object)
- [Select or Deselect Objects](#how-to-select-or-deselect-an-object)
- [Delete Objects](#how-to-delete-objects)
- [Edit an Object (Basic)](#how-to-edit-objects-basic)
- [Select a Vertex, Edge or Face](#how-to-select-a-vertex-edge-or-face)
- [Edit an Object (Complex)](#how-to-edit-objects-complex)
- [Cheat Context](#how-to-cheat-context)
- [Create and Assign a Material](#how-to-create-and-assign-a-material)
- [Create and Edit a Shader Node Tree](#how-to-create-and-edit-a-shader-node-tree)
- [Turn a Function into an Operator](#how-to-turn-a-function-into-an-operator)
- [Activate or Deactivate Addons](#how-to-activate-or-deactivate-addons)
- [Add and Edit Modifiers](#how-to-add-and-edit-modifiers)
- [Parent Objects](#how-to-parent-objects)
- [Install Python Libraries to Blender's Python](#how-to-install-python-libraries-to-blenders-python)

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
[(back to top)](#table-of-contents)

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
[(back to top)](#table-of-contents)

## How to Delete Objects
```python
import bpy

'''Delete the Active Object'''

# First you must ensure only the objects
# you want to delete are selected

# Delete
bpy.ops.object.delete()
```
[(back to top)](#table-of-contents)

## How to Edit Objects Basic
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
[(back to top)](#table-of-contents)

## How to Select a Vertex Edge or Face
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
[(back to top)](#table-of-contents)

## How to Edit Objects Complex
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
[(back to top)](#table-of-contents)

## How to Cheat Context
```python
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

```
[(back to top)](#table-of-contents)

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
[(back to top)](#table-of-contents)

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
[(back to top)](#table-of-contents)

## How to Turn a Function into an Operator
```python
import bpy

# You can rename your Operator to anything you want
# But make sure it matches the name in your register and unregister functions!
class SimplestOperator(bpy.types.Operator):
    
    # The tooltip is a multiline comment you can use to describe what your
    # Operator does, it appears when you hover the mouse
    """Tooltip"""
    
    # This tells Blender where the Operator will work and how to call it
    # This one works in Object mode, it is named simplest_operator
    # And to call it in code we use: bpy.ops.object.simplest_operator()
    # Or search for it via the F3 menu
    bl_idname = "object.simplest_operator"
    
    # This is the label that your users will see, the title
    bl_label = "Simplest Object Operator"
    
    # This is the function that will run when we call the Operator
    def execute(self, context):
        
        # Paste your code here
        
        return {'FINISHED'}


# If you changed the name of your addon above, make sure you change it here, too
def register():
    bpy.utils.register_class(SimplestOperator)


def unregister():
    bpy.utils.unregister_class(SimplestOperator)


if __name__ == "__main__":
    register()

```
[(back to top)](#table-of-contents)

## How to Activate or Deactivate Addons
```python
import bpy

'''Activate or Deactivate an Addon'''

# Activate
bpy.ops.preferences.addon_enable(module="node_arrange")

# Deactivate
bpy.ops.preferences.addon_disable(module="node_arrange")
```
[(back to top)](#table-of-contents)

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
[(back to top)](#table-of-contents)

## How to Parent Objects
```python
import bpy

'''Parent an Object'''

cube = bpy.data.objects['Cube']
camera = bpy.data.objects['Camera']

cube.parent = camera
```
[(back to top)](#table-of-contents)

## How to Install Python Libraries to Blenders Python
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
[(back to top)](#table-of-contents)

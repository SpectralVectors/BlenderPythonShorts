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
- [Setup the Simplest UI Panel](#how-to-setup-the-simplest-ui-panel)
- [Setup a Complex UI Panel](#how-to-setup-a-complex-ui-panel)
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

## How to Setup the Simplest UI Panel
```python
import bpy


class SimplestPanel(bpy.types.Panel):
    """Creates a basic UI Panel"""
    
    # Label is the Panel Title, this will appear on the Panel, itself
    bl_label = "Simplest Panel"
    
    # IDName is an internal name for Blender
    bl_idname = "VIEW_3D_PT_simplest"
    
    # This determines which area the panel will appear in, choose from:
    # ‘EMPTY’, ‘VIEW_3D’, ‘IMAGE_EDITOR’, ‘NODE_EDITOR’, ‘SEQUENCE_EDITOR’, ‘CLIP_EDITOR’, 
    # ‘DOPESHEET_EDITOR’, ‘GRAPH_EDITOR’, ‘NLA_EDITOR’, ‘TEXT_EDITOR’, ‘CONSOLE’, ‘INFO’, ‘TOPBAR’,  
    # ‘STATUSBAR’, ‘OUTLINER’, ‘PROPERTIES’, ‘FILE_BROWSER’, ‘SPREADSHEET’, ‘PREFERENCES’
    bl_space_type = 'VIEW_3D'
    
    # And this determines the region, choose from:
    # ‘WINDOW’, ‘HEADER’, ‘CHANNELS’, ‘TEMPORARY’, ‘UI’, ‘TOOLS’, ‘TOOL_PROPS’, ‘PREVIEW’, 
    # ‘HUD’, ‘NAVIGATION_BAR’, ‘EXECUTE’, ‘FOOTER’, ‘TOOL_HEADER’, ‘XR’
    bl_region_type = 'UI'
    
    # If needed you can define context, otherwise it will cause an error
    #bl_context = "object"
    
    # Needed when registering panels in the N Panel sidebar area, otherwise it will cause an error
    # This will appear on the sideways tab in the N Panel sidebar
    bl_category = "Simplest Panel"

    # Every Panel must have a draw function in order to display something on screen
    def draw(self, context):
        
        # Every draw function must start with layout
        layout = self.layout

        # Now we add a row to hold our operator
        row = layout.row()
        # Add the operator to the row and you're done!
        # This is the simplest panel you can make!
        row.operator('mesh.primitive_monkey_add')


def register():
    bpy.utils.register_class(SimplestPanel)


def unregister():
    bpy.utils.unregister_class(SimplestPanel)


if __name__ == "__main__":
    register()
```
[(back to top)](#table-of-contents)

## How to Setup a Complex UI Panel
```python
import bpy
import os
from bpy.types import WindowManager
from bpy.props import (
    StringProperty,
    EnumProperty,
)
import bpy.utils.previews

class MATERIAL_UL_matslots_example(bpy.types.UIList):
    # The draw_item function is called for each item of the collection that is visible in the list.
    #   data is the RNA object containing the collection,
    #   item is the current drawn item of the collection,
    #   icon is the "computed" icon for the item (as an integer, because some objects like materials or textures
    #   have custom icons ID, which are not available as enum items).
    #   active_data is the RNA object containing the active property for the collection (i.e. integer pointing to the
    #   active item of the collection).
    #   active_propname is the name of the active property (use 'getattr(active_data, active_propname)').
    #   index is index of the current item in the collection.
    #   flt_flag is the result of the filtering process for this item.
    #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
    #         need them.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        ob = data
        slot = item
        ma = slot.material
        # draw_item must handle the three layout types... Usually 'DEFAULT' and 'COMPACT' can share the same code.
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            # You should always start your row layout by a label (icon + text), or a non-embossed text field,
            # this will also make the row easily selectable in the list! The later also enables ctrl-click rename.
            # We use icon_value of label, as our given icon is an integer value, not an enum ID.
            # Note "data" names should never be translated!
            if ma:
                layout.prop(ma, "name", text="", emboss=False, icon_value=icon)
            else:
                layout.label(text="", translate=False, icon_value=icon)
        # 'GRID' layout type should be as compact as possible (typically a single icon!).
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

class ComplexPanel(bpy.types.Panel):
    """Creates a basic UI Panel"""
    
    # Label is the Panel Title
    bl_label = "Complex Panel"
    
    # IDName is an internal name for Blender
    bl_idname = "VIEW_3D_PT_complex"
    
    # This determines which area the panel will appear in, choose from:
    # ‘EMPTY’, ‘VIEW_3D’, ‘IMAGE_EDITOR’, ‘NODE_EDITOR’, ‘SEQUENCE_EDITOR’, ‘CLIP_EDITOR’, 
    # ‘DOPESHEET_EDITOR’, ‘GRAPH_EDITOR’, ‘NLA_EDITOR’, ‘TEXT_EDITOR’, ‘CONSOLE’, ‘INFO’, ‘TOPBAR’,  
    # ‘STATUSBAR’, ‘OUTLINER’, ‘PROPERTIES’, ‘FILE_BROWSER’, ‘SPREADSHEET’, ‘PREFERENCES’
    bl_space_type = 'VIEW_3D'
    
    # And this determines the region, choose from:
    # ‘WINDOW’, ‘HEADER’, ‘CHANNELS’, ‘TEMPORARY’, ‘UI’, ‘TOOLS’, ‘TOOL_PROPS’, ‘PREVIEW’, 
    # ‘HUD’, ‘NAVIGATION_BAR’, ‘EXECUTE’, ‘FOOTER’, ‘TOOL_HEADER’, ‘XR’
    bl_region_type = 'UI'
    
    # If needed you can define context, otherwise it will cause an error
    #bl_context = "object"
    
    # Needed when registering panels in the N Panel sidebar area, otherwise it will cause an error
    bl_category = "Complex Panel"


    # Every Panel must have a draw function in order to display something on screen
    def draw(self, context):
        
        # Every draw function must start with layout
        layout = self.layout
        obj = context.object
        wm = context.window_manager
        scene = bpy.context.scene

        row=layout.row()
        icon = 'TRIA_DOWN' if context.scene.column_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'column_panel_open', icon=icon, icon_only=True)
        row.label(text="Columns")                
        if context.scene.column_panel_open:

            # Now we start adding to the layout, a column lays out everything vertically
            column = layout.column()
            # For a full list of icons, enable the Icon Viewer addon
            column.label(text="Label with an icon", icon='WORLD_DATA')
            # You can use labels with or without icons
            column.operator("mesh.primitive_monkey_add")
            column.prop(scene, "frame_start")

        row=layout.row()
        icon = 'TRIA_DOWN' if context.scene.row_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'row_panel_open', icon=icon, icon_only=True)
        row.label(text="Rows")                
        if context.scene.row_panel_open:

            # Every time we write layout.row (or box, column etc) we start a new UI element
            row = layout.row()
            # A row lays out everything horizontally
            row.label(text='Operators:')
            # Operators appear as buttons the user can press to call the operator
            row.operator("mesh.primitive_monkey_add")
            row.prop(scene, "frame_start")

        row=layout.row()
        icon = 'TRIA_DOWN' if context.scene.box_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'box_panel_open', icon=icon, icon_only=True)
        row.label(text="Boxes")                
        if context.scene.box_panel_open:

            # Boxes provide a way to separate different parts of your UI
            box = layout.box()
            # You can combine columns, rows and boxes to create your ideal layout
            row = box.row()
            # Like columns and rows, you can put in labels, operators or properties
            row.label(text="Row label in box")
            row.operator(text='MonkeyBusiness', operator="mesh.primitive_monkey_add")
            row.prop(scene, "frame_start")
            column = box.column()
            column.label(text="Column label in box")
            column.operator(text='Cubism', operator="mesh.primitive_cube_add")
            column.prop(scene, "frame_start")
        
        row=layout.row()
        icon = 'TRIA_DOWN' if context.scene.list_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'list_panel_open', icon=icon, icon_only=True)
        row.label(text="Lists")                
        if context.scene.list_panel_open:

            # template_list now takes two new args.
            # The first one is the identifier of the registered UIList to use (if you want only the default list,
            # with no custom draw code, use "UI_UL_list").
            layout.template_list("MATERIAL_UL_matslots_example", "", obj, "material_slots", obj, "active_material_index")

            # The second one can usually be left as an empty string.
            # It's an additional ID used to distinguish lists in case you
            # use the same list several times in a given area.
            layout.template_list("MATERIAL_UL_matslots_example", "compact", obj, "material_slots",
                                obj, "active_material_index", type='COMPACT')

        row=layout.row()
        icon = 'TRIA_DOWN' if context.scene.enum_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'enum_panel_open', icon=icon, icon_only=True)
        row.label(text="Enums")                
        if context.scene.enum_panel_open:

            row = layout.row()
            row.prop(wm, "my_previews_dir")

            row = layout.row()
            row.template_icon_view(wm, "my_previews")

            row = layout.row()
            row.prop(wm, "my_previews")

def enum_previews_from_directory_items(self, context):
    """EnumProperty callback"""
    enum_items = []

    if context is None:
        return enum_items

    wm = context.window_manager
    directory = wm.my_previews_dir

    # Get the preview collection (defined in register func).
    pcoll = preview_collections["main"]

    if directory == pcoll.my_previews_dir:
        return pcoll.my_previews

    print("Scanning directory: %s" % directory)

    if directory and os.path.exists(directory):
        # Scan the directory for png files
        image_paths = []
        for fn in os.listdir(directory):
            if fn.lower().endswith(".png"):
                image_paths.append(fn)

        for i, name in enumerate(image_paths):
            # generates a thumbnail preview for a file.
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            if not icon:
                thumb = pcoll.load(name, filepath, 'IMAGE')
            else:
                thumb = pcoll[name]
            enum_items.append((name, name, "", thumb.icon_id, i))

    pcoll.my_previews = enum_items
    pcoll.my_previews_dir = directory
    return pcoll.my_previews

classes=[
    MATERIAL_UL_matslots_example,
    ComplexPanel,
]

preview_collections = {}


def register():
    
    bpy.types.Scene.column_panel_open = bpy.props.BoolProperty(
    default=False
    )

    bpy.types.Scene.row_panel_open = bpy.props.BoolProperty(
    default=False
    )

    bpy.types.Scene.list_panel_open = bpy.props.BoolProperty(
    default=False
    )

    bpy.types.Scene.enum_panel_open = bpy.props.BoolProperty(
    default=False
    )

    bpy.types.Scene.box_panel_open = bpy.props.BoolProperty(
    default=False
    )
    
    for cls in classes:
        bpy.utils.register_class(cls)

    WindowManager.my_previews_dir = StringProperty(
        name="Folder Path",
        subtype='DIR_PATH',
        default=""
    )

    WindowManager.my_previews = EnumProperty(
        items=enum_previews_from_directory_items,
    )

    # Note that preview collections returned by bpy.utils.previews
    # are regular Python objects - you can use them to store custom data.
    #
    # This is especially useful here, since:
    # - It avoids us regenerating the whole enum over and over.
    # - It can store enum_items' strings
    #   (remember you have to keep those strings somewhere in py,
    #   else they get freed and Blender references invalid memory!).
    pcoll = bpy.utils.previews.new()
    pcoll.my_previews_dir = ""
    pcoll.my_previews = ()

    preview_collections["main"] = pcoll

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    from bpy.types import WindowManager

    del WindowManager.my_previews

    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()


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

string = bpy.app.version_string
blenderversion = string.rstrip(string[-2:])

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
        f"--target=C:\\Program Files\\Blender Foundation\\Blender {blenderversion}\\{blenderversion}\\python\\lib", 
        package])
```
[(back to top)](#table-of-contents)

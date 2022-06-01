# BlenderPythonShorts
A Collection of basic scripts to help beginners with Blender Python - bpy

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

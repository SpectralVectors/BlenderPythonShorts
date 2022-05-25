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

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
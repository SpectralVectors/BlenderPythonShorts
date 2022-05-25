import bpy

'''Activate or Deactivate an Addon'''

# Activate
bpy.ops.preferences.addon_enable(module="node_arrange")

# Deactivate
bpy.ops.preferences.addon_disable(module="node_arrange")

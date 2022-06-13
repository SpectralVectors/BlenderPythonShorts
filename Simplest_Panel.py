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

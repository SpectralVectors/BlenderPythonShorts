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

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

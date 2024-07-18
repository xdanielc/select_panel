# ----- BEGIN GPL LICENSE BLOCK -----
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ----- END GPL LICENSE BLOCK -----

from bpy.ops import text
from bpy.props import StringProperty
from bpy.types import AddonPreferences
import bpy
bl_info = {
    "name": "Select panel",
    "author": "Daniel Calderón",
    "description": "Select Panel",
    "blender": (2, 80, 0),
    "version": (0, 1, 6),
    "location": "3D View > Toolbox > Select tab",
    "warning": "",
    "doc_url": "https://github.com/xdanielc/select_panel",
    "category": "User Interface"
}


class VIEW3D_PT_Obj_Select(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Select"
    bl_idname = "VIEW3D_PT_obj_select"
    bl_label = "Select Panel"
    bl_context = "objectmode"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        layout = self.layout

        layout.label(text="Select")
        col = layout.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator("object.select_all", text="All").action = 'SELECT'
        row.operator("object.select_all", text="None").action = 'DESELECT'
        row.operator("object.select_all", text="Invert").action = 'INVERT'

        layout.label(text="select")
        col = layout.column(align=True)
        col.scale_y = 1.5
        row = col.row(align=True)
        row.operator("view3d.select_box", text="Box")
        row.operator("view3d.select_circle", text="Brush")

        col = layout.column(align=True)
        col.scale_y = 1.5
        row = col.row(align=True)
        row.operator("object.select_camera", text="Camera")
        row.operator("object.select_mirror", text="Mirror")
        row.operator("object.select_random", text="Random")

        col = layout.column(align=True)
        col.scale_y = 1.5
        row = col.row(align=True)
        row.operator("object.select_more", text="Parent/Child +")
        row.operator("object.select_less", text="Parent/Child -")

        col = layout.column(align=True)
        col.scale_y = 1.5
        col.operator_menu_enum("object.select_by_type", "type", text="Type...")
        col.operator_menu_enum("object.select_grouped", "type", text="Grouped...")
        col.operator_menu_enum("object.select_linked", "type", text="Linked...")
        col.operator("object.select_pattern", text="Search name")


class VIEW3D_PT_Mesh_Select(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Select"
    bl_idname = "VIEW3D_PT_mesh_select"
    bl_label = "Select Panel"
    bl_context = "mesh_edit"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        layout = self.layout

        layout.label(text="Select")
        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.select_all", text="All").action = 'SELECT'
        row.operator("mesh.select_all", text="None").action = 'DESELECT'
        row.operator("mesh.select_all", text="Invert").action = 'INVERT'

        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("view3d.select_box", text="Box")
        row.operator("view3d.select_circle", text="Circle")

        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.select_random", text="Random")
        row.operator("mesh.select_nth", text="Checker Des")

        col = layout.column(align=True)
        col.scale_y = 1.3
        col.operator("mesh.edges_select_sharp")

        col = layout.column(align=True)
        col.scale_y = 1.3
        col.operator("mesh.select_similar", text="Similar")

        col = layout.column(align=True)
        col.scale_y = 1.3
        row = col.row(align=True)
        row.operator("mesh.select_non_manifold", text="Non Manifold")
        row.operator("mesh.select_loose", text="Loose")
        row = col.row(align=True)
        row.operator("mesh.select_interior_faces", text="Interior faces")
        row.operator("mesh.select_face_by_sides", text="By sides")
        col.operator("mesh.select_ungrouped", text="Ungrouped verts")

        col = layout.column(align=True)
        col.scale_y = 2
        row = col.row(align=True)
        row.scale_x = 4
        row.operator("mesh.select_more", text="", icon="ADD")
        row.operator("mesh.select_less", text="", icon="REMOVE")
        row.operator("mesh.select_next_item", text="", icon="FRAME_NEXT")
        row.operator("mesh.select_prev_item", text="", icon="FRAME_PREV")

        col = layout.column(align=True)
        col.scale_y = 1.3
        row = col.row(align=True)
        row.operator("mesh.loop_multi_select", text="Loop").ring = False
        row.operator("mesh.loop_multi_select", text="Ring").ring = True
        row = col.row(align=True)
        row.operator("mesh.loop_to_region", text="Loop inner region").select_bigger = False
        row.operator("mesh.region_to_loop", text="Boundary Loop")

        row = layout.row(align=True)
        row.scale_y = 1.3
        row.operator("mesh.select_linked", text="Linked")
        row.operator("mesh.shortest_path_select", text="Shortest")
        row.operator("mesh.faces_select_linked_flat", text="Coplanar")
        row = layout.row(align=True)
        row.scale_y = 1.3
        if operator_exists("mesh.adj_verices"):
            row.operator("mesh.adj_verices", text="adj vertices")
            row.operator("mesh.adj_edges", text="adj edges")
            row.operator("mesh.adj_polygons", text="adj faces")

        col = layout.column(align=True)
        col.scale_y = 1.3
        col.operator("mesh.select_axis")
        col.operator("mesh.select_mirror")
        if operator_exists("mesh.ext_deselect_boundary"):
            col.operator("mesh.ext_deselect_boundary")
        if operator_exists("mesh.pivot_set"):
            col.operator("mesh.pivot_set", text="Pivot")


class VIEW3D_PT_VertexGroups(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Select"
    bl_idname = "VIEW3D_PT_vertex_groups_select"
    bl_label = "Vertex Groups"
    bl_context = "mesh_edit"

    def draw(self, context):
        layout = self.layout

        ob = context.object
        group = ob.vertex_groups.active

        rows = 3
        if group:
            rows = 5

        row = layout.row()
        row.template_list("MESH_UL_vgroups", "", ob, "vertex_groups", ob.vertex_groups, "active_index", rows=rows)

        col = row.column(align=True)

        col.operator("object.vertex_group_add", icon='ADD', text="")
        props = col.operator("object.vertex_group_remove", icon='REMOVE', text="")
        props.all_unlocked = props.all = False

        col.separator()

        col.menu("MESH_MT_vertex_group_context_menu", icon='DOWNARROW_HLT', text="")

        if group:
            col.separator()
            col.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
            col.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

        if ob.vertex_groups and (ob.mode == 'EDIT' or (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex)):
            row = layout.row()

            sub = row.row(align=True)
            sub.operator("object.vertex_group_assign", text="Assign")
            sub.operator("object.vertex_group_remove_from", text="Remove")

            sub = row.row(align=True)
            sub.operator("object.vertex_group_select", text="Select")
            sub.operator("object.vertex_group_deselect", text="Deselect")

            layout.prop(context.tool_settings, "vertex_group_weight", text="Weight")


# Add-ons Preferences Update Panel

# Define Panel classes for updating
panels = (
    VIEW3D_PT_Obj_Select,
    VIEW3D_PT_Mesh_Select,
    VIEW3D_PT_VertexGroups
)


def update_panel(self, context):
    message = "Select Panel: Updating Panel locations has failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            panel.bl_category = context.preferences.addons[__name__].preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass


class SelectPanelPreferences(AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    category: StringProperty(
        name="Tab Category",
        description="Choose a name for the category of the panel",
        default="Select",
        update=update_panel
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.label(text="Tab Category:")
        col.prop(self, "category", text="")

        row = layout.row()
        row.label(text="Recommended addons")

        row = layout.row()
        if not operator_exists("mesh.adj_verices"):
            row.label(text="Adjacent selection", icon='ERROR')
        else:
            row.label(text="Adjacent selection", icon='CHECKMARK')
        row.operator("wm.url_open", text="URL", icon='URL').url = "https://github.com/Borschberry/Adjacent-Selection"

        row = layout.row()
        if not operator_exists("mesh.ext_deselect_boundary"):
            row.label(text="Edit Mesh Tools", icon='ERROR')
        else:
            row.label(text="Edit Mesh Tools", icon='CHECKMARK')
        row.label(text="Addon installed with blender", icon='INFO')

        row = layout.row()
        if not operator_exists("mesh.pivot_set"):
            row.label(text="xdanic utilities", icon='ERROR')
        else:
            row.label(text="xdanic utilities", icon='CHECKMARK')
        row.operator("wm.url_open", text="URL", icon='URL').url = "https://github.com/xdanielc"

        col = layout.column()
        col.label(text="Shortchuts added:")
        col.label(text="Select islands with double click and shift double click")
        col.label(text="Select more or less with shift ctrl + mouse wheel")
        col.label(text="Select next or prev with shift + mouse wheel")


def operator_exists(idname):
    names = idname.split(".")
    a = bpy.ops
    for prop in names:
        a = getattr(a, prop)
        
    try:
        name = a.__repr__()
        return True
    except:
        return False

classes = (
    VIEW3D_PT_Obj_Select,
    VIEW3D_PT_Mesh_Select,
    VIEW3D_PT_VertexGroups,
    SelectPanelPreferences
)

addon_keymaps = []

# Register all operators and panels
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Name "mesh" is inside 3D view, but space_type should be set as empty to work
        km = kc.keymaps.new(name='Mesh', space_type='EMPTY')
        kmi = km.keymap_items.new("mesh.select_linked", 'LEFTMOUSE', 'DOUBLE_CLICK')
        kmi = km.keymap_items.new("mesh.select_linked", 'LEFTMOUSE', 'DOUBLE_CLICK', shift=True)
        kmi = km.keymap_items.new("mesh.select_more", 'WHEELUPMOUSE', 'PRESS', shift=True, ctrl=True)
        kmi = km.keymap_items.new("mesh.select_less", 'WHEELDOWNMOUSE', 'PRESS', shift=True, ctrl=True)
        kmi = km.keymap_items.new("mesh.select_next_item", 'WHEELUPMOUSE', 'PRESS', shift=True)
        kmi = km.keymap_items.new("mesh.select_prev_item", 'WHEELDOWNMOUSE', 'PRESS', shift=True)

    update_panel(None, bpy.context)


def unregister():
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
        addon_keymaps.clear()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

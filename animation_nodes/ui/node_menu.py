import bpy
from bpy.props import *
from .. utils.operators import makeOperator
from .. sockets.info import getBaseDataTypes
from .. tree_info import getSubprogramNetworks
from .. utils.nodes import getAnimationNodeTrees

mainBaseDataTypes = ("Object", "Integer", "Float", "Vector", "Text")
numericalDataTypes = ("Matrix", "Vector", "Float", "Color", "Euler", "Quaternion")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if drawNodeTreeChooser(layout, context):
        return

    layout.operator("an.node_search", text = "Search", icon = "VIEWZOOM")
    layout.separator()
    layout.menu("AN_MT_number_menu", text = "Number", icon = "LINENUMBERS_ON")
    layout.menu("AN_MT_vector_menu", text = "Vector", icon = "EXPORT")
    layout.menu("AN_MT_rotation_menu", text = "Rotation", icon = "FILE_REFRESH")
    layout.menu("AN_MT_matrix_menu", text = "Matrix", icon = "GRID")
    layout.menu("AN_MT_text_menu", text = "Text", icon = "SORTALPHA")
    layout.menu("AN_MT_boolean_menu", text = "Boolean", icon = "CHECKBOX_HLT")
    layout.menu("AN_MT_color_menu", text = "Color", icon = "COLOR")
    layout.menu("AN_MT_list_menu", text = "List", icon = "WORDWRAP_ON")
    layout.separator()
    layout.menu("AN_MT_object_menu", text = "Object", icon = "OBJECT_DATAMODE")
    layout.menu("AN_MT_mesh_menu", text = "Mesh", icon = "MESH_DATA")
    layout.menu("AN_MT_spline_menu", text = "Spline", icon = "CURVE_DATA")
    layout.menu("AN_MT_gpencil_menu", text = "Grease Pencil", icon = "OUTLINER_OB_GREASEPENCIL")
    layout.menu("AN_MT_particle_system_menu", text = "Particle System", icon = "PARTICLE_DATA")
    layout.separator()
    layout.menu("AN_MT_animation_menu", text = "Animation", icon = "RENDER_ANIMATION")
    layout.menu("AN_MT_interpolation_menu", text = "Interpolation", icon = "IPO_BEZIER")
    layout.menu("AN_MT_falloff_menu", text = "Falloff", icon = "SMOOTHCURVE")
    layout.menu("AN_MT_action_menu", text = "Action", icon = "ANIM_DATA")
    layout.menu("AN_MT_fcurve_menu", text = "FCurves", icon = "FCURVE")
    layout.menu("AN_MT_material_menu", text = "Material", icon = "NODE_MATERIAL")
    layout.menu("AN_MT_sound_menu", text = "Sound", icon = "SPEAKER")
    layout.menu("AN_MT_sequence_menu", text = "Sequence", icon = "SEQUENCE")
    layout.separator()
    layout.menu("AN_MT_geometry_menu", text = "Geometry", icon = "ORIENTATION_NORMAL")
    layout.menu("AN_MT_kdtree_bvhtree_menu", text = "KD & BVH Tree", icon = "STICKY_UVS_LOC")
    layout.separator()
    layout.menu("AN_MT_viewer_menu", text = "Viewer", icon = "INFO")
    layout.menu("AN_MT_subprograms_menu", text = "Subprograms", icon = "FILE_SCRIPT")
    layout.menu("AN_MT_layout_menu", text = "Layout", icon = "IMGDISPLAY")

def drawNodeTreeChooser(layout, context):
    if len(getAnimationNodeTrees()) == 0:
        col = layout.column()
        col.scale_y = 1.6
        col.operator("an.create_node_tree", text = "New Node Tree", icon = "PLUS")
        return True
    return False

@makeOperator("an.create_node_tree", "Create Node Tree")
def createNodeTree():
    tree = bpy.data.node_groups.new("AN Tree", "an_AnimationNodeTree")
    bpy.context.space_data.node_tree = tree

class NumberMenu(bpy.types.Menu):
    bl_idname = "AN_MT_number_menu"
    bl_label = "Number Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Integer", {"assignedType" : repr("Integer")})
        insertNode(layout, "an_DataInputNode", "Float", {"assignedType" : repr("Float")})
        insertNode(layout, "an_CreateListNode", "Integer List", {"assignedType" : repr("Integer")})
        insertNode(layout, "an_CreateListNode", "Float List", {"assignedType" : repr("Float")})
        insertNode(layout, "an_NumberRangeNode", "Integer Range", {"dataType" : repr("Integer")})
        insertNode(layout, "an_NumberRangeNode", "Float Range", {"dataType" : repr("Float")})
        insertNode(layout, "an_ParseNumberNode", "Parse Number")
        insertNode(layout, "an_NumberConstantsNode", "Constants")
        layout.separator()
        insertNode(layout, "an_RandomNumberNode", "Random")
        insertNode(layout, "an_FloatWiggleNode", "Wiggle")
        insertNode(layout, "an_MixDataNode", "Mix", {"dataType" : repr("Float")})
        insertNode(layout, "an_MapRangeNode", "Map Range")
        layout.separator()
        insertNode(layout, "an_FloatMathNode", "Math")
        insertNode(layout, "an_NumberListMathNode", "List Math")
        insertNode(layout, "an_SortNumbersNode", "Sort Numbers")
        insertNode(layout, "an_FloatClampNode", "Clamp")
        insertNode(layout, "an_RoundNumberNode", "Round")
        insertNode(layout, "an_ConvertAngleNode", "Convert Angle")
        insertNode(layout, "an_FloatToIntegerNode", "Float to Integer")
        insertNode(layout, "an_FloatToTextNode", "Float to Text")

class VectorMenu(bpy.types.Menu):
    bl_idname = "AN_MT_vector_menu"
    bl_label = "Vector Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SeparateVectorNode", "Separate")
        insertNode(layout, "an_CombineVectorNode", "Combine")
        insertNode(layout, "an_VectorFromValueNode", "From Value")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Vector")})
        layout.separator()
        insertNode(layout, "an_RandomVectorNode", "Random")
        insertNode(layout, "an_VectorWiggleNode", "Wiggle")
        insertNode(layout, "an_VectorNoiseNode", "Noise")
        insertNode(layout, "an_MixDataNode", "Mix", {"dataType" : repr("Vector")})
        layout.separator()
        insertNode(layout, "an_VectorDistanceNode", "Distance")
        insertNode(layout, "an_ProjectPointOnLineNode", "Distance to Line")
        insertNode(layout, "an_ProjectPointOnPlaneNode", "Distance to Plane")
        layout.separator()
        insertNode(layout, "an_VectorAngleNode", "Angle")
        insertNode(layout, "an_VectorLengthNode", "Length")
        insertNode(layout, "an_VectorDotProductNode", "Dot Product")
        layout.separator()
        insertNode(layout, "an_VectorMathNode", "Math")
        insertNode(layout, "an_VectorListMathNode", "List Math")
        insertNode(layout, "an_TransformVectorNode", "Transform")
        insertNode(layout, "an_OffsetVectorNode", "Offset", {"useVectorList" : repr(True)})

class RotationMenu(bpy.types.Menu):
    bl_idname = "AN_MT_rotation_menu"
    bl_label = "Rotation Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DirectionToRotationNode", "Direction to Rotation")
        insertNode(layout, "an_RotationToDirectionNode", "Rotation to Direction")
        insertNode(layout, "an_ConvertVectorAndEulerNode", "Euler to/from Vector")
        insertNode(layout, "an_ConvertRotationsNode", "Convert Rotation Types", {"conversionType" : repr("MATRIX_TO_EULER")})
        layout.separator()
        insertNode(layout, "an_SeparateEulerNode", "Separate Euler")
        insertNode(layout, "an_CombineEulerNode", "Combine Euler")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Euler")})
        layout.separator()
        insertNode(layout, "an_EulerMathNode", "Euler Math")
        insertNode(layout, "an_MixDataNode", "Euler Mix", {"dataType" : repr("Euler")})
        insertNode(layout, "an_RandomEulerNode", "Random Euler")
        insertNode(layout, "an_EulerWiggleNode", "Euler Wiggle")
        layout.separator()
        insertNode(layout, "an_SeparateQuaternionNode", "Separate Quaternion")
        insertNode(layout, "an_CombineQuaternionNode", "Combine Quaternion")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Quaternion")})
        layout.separator()
        insertNode(layout, "an_QuaternionMathNode", "Quaternion Math")
        insertNode(layout, "an_MixDataNode", "Quaternion Mix", {"dataType" : repr("Quaternion")})
        insertNode(layout, "an_RandomQuaternionNode", "Random Quaternion")
        insertNode(layout, "an_QuaternionWiggleNode", "Quaternion Wiggle")
        layout.separator()
        insertNode(layout, "an_QuaternionListCombineNode", "Combine Quaternion Rotations")


class MatrixMenu(bpy.types.Menu):
    bl_idname = "AN_MT_matrix_menu"
    bl_label = "Matrix Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ComposeMatrixNode", "Compose")
        insertNode(layout, "an_DecomposeMatrixNode", "Decompose")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Matrix")})
        layout.separator()
        insertNode(layout, "an_DistributeMatricesNode", "Distribute")
        insertNode(layout, "an_ReplicateMatrixNode", "Replicate")
        insertNode(layout, "an_TransformMatrixNode", "Transform")
        insertNode(layout, "an_InvertMatrixNode", "Invert")
        insertNode(layout, "an_MixDataNode", "Mix", {"dataType" : repr("Matrix")})
        layout.separator()
        insertNode(layout, "an_ShearMatrixNode", "Shear")
        insertNode(layout, "an_AxisRotationMatrixNode", "Axis Rotation")
        insertNode(layout, "an_ExtractMatrixBasisNode", "Extract Matrix Basis")
        layout.separator()
        insertNode(layout, "an_MatrixMathNode", "Math")
        insertNode(layout, "an_MatrixCombineNode", "Combine")
        insertNode(layout, "an_OffsetMatrixNode", "Offset", {"useMatrixList" : repr(True)})

class TextMenu(bpy.types.Menu):
    bl_idname = "AN_MT_text_menu"
    bl_label = "Text Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Input", {"assignedType" : repr("Text")})
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Text")})
        insertNode(layout, "an_RandomTextNode", "Random")
        insertNode(layout, "an_CharactersNode", "Characters")
        insertNode(layout, "an_ConvertToTextNode", "Convert To Text")
        insertNode(layout, "an_TimecodeGeneratorNode", "Timecode Generator")
        layout.separator()
        insertNode(layout, "an_SplitTextNode", "Split")
        insertNode(layout, "an_JoinTextsNode", "Join")
        insertNode(layout, "an_TrimTextNode", "Trim")
        insertNode(layout, "an_ChangeTextCaseNode", "Change Text Case")
        layout.separator()
        insertNode(layout, "an_ReverseTextNode", "Reverse")
        insertNode(layout, "an_ReplaceTextNode", "Replace")
        insertNode(layout, "an_RepeatTextNode", "Repeat")
        insertNode(layout, "an_TextLengthNode", "Length")
        layout.separator()
        insertNode(layout, "an_LSystemNode", "LSystem")
        insertNode(layout, "an_DecomposeTextNode", "Decompose Text")
        layout.separator()
        insertNode(layout, "an_TextBlockReaderNode", "Block Reader")
        insertNode(layout, "an_TextBlockWriterNode", "Block Writer")
        insertNode(layout, "an_FilterBlendDataListByNameNode", "Filter Text Block List", {"dataType" : repr("Text Block")})
        insertNode(layout, "an_TextFileReaderNode", "File Reader")
        layout.separator()
        insertNode(layout, "an_TextSequenceOutputNode", "Sequence Output")
        insertNode(layout, "an_CharacterPropertiesOutputNode", "Character Property")
        insertNode(layout, "an_SeparateTextObjectNode", "Object Separate")
        insertNode(layout, "an_TextObjectOutputNode", "Object Output")

class BooleanMenu(bpy.types.Menu):
    bl_idname = "AN_MT_boolean_menu"
    bl_label = "Boolean Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Boolean", {"assignedType" : repr("Boolean")})
        insertNode(layout, "an_InvertBooleanNode", "Invert")
        insertNode(layout, "an_CompareNode", "Compare")
        insertNode(layout, "an_CompareNumbersNode", "Compare Numbers")
        insertNode(layout, "an_SwitchNode", "Switch")
        insertNode(layout, "an_LogicOperatorsNode", "Logic")
        insertNode(layout, "an_BooleanListLogicNode", "List Logic")
        insertNode(layout, "an_RandomBooleanNode", "Random Boolean")

class ColorMenu(bpy.types.Menu):
    bl_idname = "AN_MT_color_menu"
    bl_label = "Color Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ChooseColorNode", "Choose Color")
        insertNode(layout, "an_CombineColorNode", "Combine Color")
        insertNode(layout, "an_SeparateColorNode", "Separate Color")
        insertNode(layout, "an_MixDataNode", "Mix", {"dataType" : repr("Color")})
        insertNode(layout, "an_RandomColorNode", "Random Color")
        layout.separator()
        insertNode(layout, "an_SetVertexColorNode", "Set Vertex Color")

class ListMenu(bpy.types.Menu):
    bl_idname = "AN_MT_list_menu"
    bl_label = "List Menu"

    def draw(self, context):
        layout = self.layout
        layout.menu("AN_MT_create_list_menu", text = "Create")
        layout.menu("AN_MT_combine_list_menu", text = "Combine")
        insertNode(layout, "an_AppendListNode", "Append")
        insertNode(layout, "an_InsertListElementNode", "Insert")
        layout.separator()
        insertNode(layout, "an_GetListElementNode", "Get Element")
        insertNode(layout, "an_GetRandomListElementsNode", "Get Random Elements")
        insertNode(layout, "an_SearchListElementNode", "Search Element")
        insertNode(layout, "an_SetListElementNode", "Set Element")
        insertNode(layout, "an_RemoveListElementNode", "Remove Element")
        layout.separator()
        insertNode(layout, "an_GetListLengthNode", "Get Length")
        layout.separator()
        insertNode(layout, "an_ShuffleListNode", "Shuffle")
        insertNode(layout, "an_ReverseListNode", "Reverse")
        insertNode(layout, "an_SliceListNode", "Slice")
        insertNode(layout, "an_ShiftListNode", "Shift")
        insertNode(layout, "an_MaskListNode", "Mask")
        layout.separator()
        insertNode(layout, "an_FillListNode", "Fill")
        insertNode(layout, "an_RepeatListNode", "Repeat")
        insertNode(layout, "an_RepeatListElementsNode", "Repeat Elements")
        insertNode(layout, "an_RandomListNode", "Random")
        insertNode(layout, "an_ListBooleanOperationsNode", "List Boolean Operations")
        layout.separator()
        insertNode(layout, "an_SetStructElementsNode", "Set Struct Elements")
        insertNode(layout, "an_GetStructElementsNode", "Get Struct Elements")
        insertNode(layout, "an_GetStructListElementsNode", "Get Struct List Elements")


class CreateListMenu(bpy.types.Menu):
    bl_idname = "AN_MT_create_list_menu"
    bl_label = "Create List Menu"

    def draw(self, context):
        layout = self.layout
        for dataType in mainBaseDataTypes:
            insertNode(layout, "an_CreateListNode", dataType, {"assignedType" : repr(dataType)})
        layout.separator()
        layout.menu("AN_MT_create_list_menu_extended", text = "More")

class CreateListMenuExtended(bpy.types.Menu):
    bl_idname = "AN_MT_create_list_menu_extended"
    bl_label = "Create List Menu Extended"

    def draw(self, context):
        layout = self.layout
        for dataType in sorted(getBaseDataTypes()):
            if dataType not in mainBaseDataTypes:
                insertNode(layout, "an_CreateListNode", dataType, {"assignedType" : repr(dataType)})

class CombineListMenu(bpy.types.Menu):
    bl_idname = "AN_MT_combine_list_menu"
    bl_label = "Combine List Menu"

    def draw(self, context):
        layout = self.layout
        for dataType in mainBaseDataTypes:
            insertNode(layout, "an_CombineListsNode", dataType, {"assignedType" : repr(dataType)})
        layout.separator()
        layout.menu("AN_MT_combine_list_menu_extended", text = "More")

class CombineListMenuExtended(bpy.types.Menu):
    bl_idname = "AN_MT_combine_list_menu_extended"
    bl_label = "Combine List Menu Extended"

    def draw(self, context):
        layout = self.layout
        for dataType in sorted(getBaseDataTypes()):
            if dataType not in mainBaseDataTypes:
                insertNode(layout, "an_CombineListsNode", dataType, {"assignedType" : repr(dataType)})

class ObjectMenu(bpy.types.Menu):
    bl_idname = "AN_MT_object_menu"
    bl_label = "Object Menu"

    def draw(self, context):
        layout = self.layout

        insertNode(layout, "an_DataInputNode", "Object", {"assignedType" : repr("Object")})
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Object")})
        insertNode(layout, "an_FilterBlendDataListByNameNode", "Filter Object List", {"dataType" : repr("Object")})
        layout.menu("AN_MT_collection_menu", text = "Collection")
        layout.separator()
        insertNode(layout, "an_ObjectTransformsInputNode", "Transforms Input")
        insertNode(layout, "an_ObjectTransformsOutputNode", "Transforms Output")
        insertNode(layout, "an_ObjectMatrixInputNode", "Matrix Input")
        insertNode(layout, "an_ObjectMatrixOutputNode", "Matrix Output")
        insertNode(layout, "an_ObjectAttributeInputNode", "Attribute Input")
        insertNode(layout, "an_ObjectAttributeOutputNode", "Attribute Output")
        insertNode(layout, "an_ObjectColorOutputNode", "Color Output")
        insertNode(layout, "an_ObjectDataPathOutputNode", "Data Path Output")
        layout.separator()
        insertNode(layout, "an_ObjectVisibilityInputNode", "Visibility Input")
        insertNode(layout, "an_ObjectVisibilityOutputNode", "Visibility Output")
        layout.separator()
        insertNode(layout, "an_LampInputNode", "Lamp Input")
        insertNode(layout, "an_LampOutputNode", "Lamp Output")
        layout.separator()
        insertNode(layout, "an_ShapeKeysFromObjectNode", "Shape Keys from Object")
        insertNode(layout, "an_ShapeKeyOutputNode", "Shape Key Output")
        layout.separator()
        insertNode(layout, "an_EvaluateObjectNode", "Evaluate Object")
        layout.separator()
        insertNode(layout, "an_ObjectIDKeyNode", "ID Key")
        insertNode(layout, "an_CopyObjectDataNode", "Copy Data")
        insertNode(layout, "an_CopyObjectModifiersNode", "Copy Modifiers")
        insertNode(layout, "an_SetKeyframesNode", "Set Keyframes")
        insertNode(layout, "an_ArmatureInfoNode", "Armature Info")
        layout.menu("AN_MT_object_utils_menu", text = "Utils")
        layout.separator()
        insertNode(layout, "an_ObjectInstancerNode", "Instancer")
        layout.separator()
        insertNode(layout, "an_SetCustomAttributeNode", " Set Custom Attribute")

class ObjectUtilsMenu(bpy.types.Menu):
    bl_idname = "AN_MT_object_utils_menu"
    bl_label = "Object Utils Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_MoveObjectNode", "Move")
        insertNode(layout, "an_TransformObjectNode", "Transform")
        insertNode(layout, "an_ResetObjectTransformsNode", "Reset Transformations")
        insertNode(layout, "an_CopyTransformsNode", "Copy Transformations")
        insertNode(layout, "an_GetSelectedObjectsNode", "Get Selected Objects")
        insertNode(layout, "an_GetActiveCameraNode", "Get Active Camera")

class CollectionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_collection_menu"
    bl_label = "Collection Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Collection", {"assignedType" : repr("Collection")})
        insertNode(layout, "an_CollectionInfoNode", "Collection Info")
        insertNode(layout, "an_CollectionOperationsNode", "Collection Operations")
        insertNode(layout, "an_BlendDataByNameNode", "Collection By Name", {"dataType" : repr("Collection")})
        insertNode(layout, "an_CreateListNode", "Create Collection List", {"assignedType" : repr("Collection")})
        insertNode(layout, "an_CombineListsNode", "Combine Collection Lists", {"assignedType" : repr("Collection")})
        insertNode(layout, "an_FilterBlendDataListByNameNode", "Filter Collection List", {"dataType" : repr("Collection")})

class MeshMenu(bpy.types.Menu):
    bl_idname = "AN_MT_mesh_menu"
    bl_label = "Mesh Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_MeshObjectInputNode", "Mesh Input")
        insertNode(layout, "an_MeshInfoNode", "Mesh Info")
        insertNode(layout, "an_ObjectBoundingBoxNode", "Get Bounding Box")
        insertNode(layout, "an_CombineMeshNode", "Combine Mesh")
        insertNode(layout, "an_MeshFromSplineNode", "Mesh From Spline")
        layout.separator()
        layout.menu("AN_MT_mesh_data_menu", text = "Mesh Data")
        layout.separator()
        insertNode(layout, "an_OffsetPolygonsNode", "Offset Polygons")
        insertNode(layout, "an_SeparatePolygonsNode", "Separate Polygons")
        insertNode(layout, "an_ExtractPolygonTransformsNode", "Extract Polygon Transforms")
        insertNode(layout, "an_OffsetVerticesNode", "Offset Vertices")
        insertNode(layout, "an_TransformMeshNode", "Transform Mesh")
        insertNode(layout, "an_TriangulateMeshNode", "Triangulate Mesh")
        layout.menu("AN_MT_mesh_generators_menu", text = "Generators")
        layout.menu("AN_MT_mesh_operators_menu", text = "Operators")
        layout.separator()
        insertNode(layout, "an_CreateListNode", "Mesh List", {"assignedType" : repr("Mesh")})
        insertNode(layout, "an_JoinMeshListNode", "Join Mesh List")
        insertNode(layout, "an_BMeshMeshNode", "BMesh Mesh")
        insertNode(layout, "an_CreateBMeshFromMeshNode", "BMesh from Mesh")
        insertNode(layout, "an_BMeshFromObjectNode", "BMesh from Object")
        layout.menu("AN_MT_mesh_finalizing_menu", text = "Tools")
        layout.separator()
        insertNode(layout, "an_MeshObjectOutputNode", "Object Output")

class MeshDataMenu(bpy.types.Menu):
    bl_idname = "AN_MT_mesh_data_menu"
    bl_label = "Mesh Data Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_VertexGroupInputNode", "Vertex Group Input")
        insertNode(layout, "an_GetVertexGroupNode", "Get Vertex Group")
        insertNode(layout, "an_InsertVertexGroupNode", "Insert Vertex Group")
        insertNode(layout, "an_SetVertexWeightNode", "Set Vertex Weight")
        insertNode(layout, "an_GetVertexColorLayerNode", "Get Vertex Color Layer")
        insertNode(layout, "an_InsertVertexColorLayerNode", "Insert Vertex Color Layer")
        insertNode(layout, "an_SetVertexColorNode", "Set Vertex Color")
        insertNode(layout, "an_SetBevelVertexWeightNode", "Set Bevel Vertex Weight")
        insertNode(layout, "an_SetBevelEdgeWeightNode", "Set Bevel Edge Weight")
        insertNode(layout, "an_SetEdgeCreaseNode", "Set Edge Crease")
        insertNode(layout, "an_GetUVMapNode", "Get UV Map")
        insertNode(layout, "an_InsertUVMapNode", "Insert UV Map")
        insertNode(layout, "an_SetUVMapNode", "Set UV Map")
        insertNode(layout, "an_SetPolygonMaterialIndexNode", "Set Polygon Material Index")
        layout.separator()
        insertNode(layout, "an_GetCustomAttributeNode", " Get Custom Attribute")
        insertNode(layout, "an_InsertCustomAttributeNode", " Insert Custom Attribute")
        insertNode(layout, "an_SetCustomAttributeNode", " Set Custom Attribute")


regularPolygons = [
    ("Regular Pentagon", 5),
    ("Regular Hexagon", 6),
    ("Regular Heptagon", 7),
    ("Regular Octagon", 8),
]

class RegularPolygonMeshGeneratorsMenu(bpy.types.Menu):
    bl_idname = "AN_MT_regular_polygon_mesh_generators_menu"
    bl_label = "Regular Polygon Mesh Generators Menu"

    def draw(self, context):
        layout = self.layout
        for name, n in regularPolygons:
            insertNode(layout, "an_CircleMeshNode", name, {'inputs["Radial Loops"].value' : repr(n)})

class MeshGeneratorsMenu(bpy.types.Menu):
    bl_idname = "AN_MT_mesh_generators_menu"
    bl_label = "Mesh Generators Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_LineMeshNode", "Line")
        insertNode(layout, "an_GridMeshNode", "Grid")
        insertNode(layout, "an_CircleMeshNode", "Circle")
        insertNode(layout, "an_CylinderMeshNode", "Cylinder")
        insertNode(layout, "an_UnityTriangleMeshNode", "Unity Triangle")
        layout.menu("AN_MT_regular_polygon_mesh_generators_menu", text = "Regular Polygons")

class MeshOperatorsMenu(bpy.types.Menu):
    bl_idname = "AN_MT_mesh_operators_menu"
    bl_label = "Mesh Operators Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_FindClosePointsNode", "Find Close Points")
        insertNode(layout, "an_FindShortestPathNode", "Find Shortest Path")
        insertNode(layout, "an_EdgeToTubeNode", "Edge to Tube")
        insertNode(layout, "an_MeshPointsScatterNode", "Scatter Points")
        layout.separator()
        insertNode(layout, "an_CreateEdgesNode", "Create Edges")
        insertNode(layout, "an_CreateEdgeIndicesNode", "Create Edge Indices")
        insertNode(layout, "an_CreatePolygonIndicesNode", "Create Polygon Indices")
        insertNode(layout, "an_EdgesOfPolygonsNode", "Edges of Polygons")
        layout.separator()
        insertNode(layout, "an_EdgeInfoNode", "Edge Info")
        insertNode(layout, "an_GetLinkedVerticesNode", "Get Linked Vertices")

class MeshFinalizingMenu(bpy.types.Menu):
    bl_idname = "AN_MT_mesh_finalizing_menu"
    bl_label = "Mesh Finalizing Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_BMeshRemoveDoublesNode", "Remove Doubles")
        insertNode(layout, "an_BMeshLimitedDissolveNode", "Limited Dissolve")
        insertNode(layout, "an_BMeshRecalculateFaceNormalsNode", "Recalculate Normals")
        insertNode(layout, "an_BMeshInvertNormalsNode", "Invert Normals")
        insertNode(layout, "an_ShadeObjectSmoothNode", "Shade Object Smooth")

class SplineMenu(bpy.types.Menu):
    bl_idname = "AN_MT_spline_menu"
    bl_label = "Spline Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SplinesFromObjectNode", "Get from Object")
        insertNode(layout, "an_SplineFromPointsNode", "Create from Points")
        insertNode(layout, "an_SplinesFromEdgesNode", "Create from Edges")
        insertNode(layout, "an_SplineFromGPStrokeNode", "Create from Stroke")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Spline")})
        insertNode(layout, "an_AppendPointToSplineNode", "Append Point")
        layout.separator()
        insertNode(layout, "an_TransformSplineNode", "Transform")
        insertNode(layout, "an_ConnectSplinesNode", "Connect")
        insertNode(layout, "an_TrimSplineNode", "Trim")
        insertNode(layout, "an_BevelSplineNode", "Bevel")
        insertNode(layout, "an_SetSplineRadiusNode", "Set Radius")
        insertNode(layout, "an_MakeSplineCyclicNode", "Make Cyclic")
        insertNode(layout, "an_SmoothBezierSplineNode", "Smooth Bezier")
        insertNode(layout, "an_TiltSplineNode", "Tilt Spline")
        insertNode(layout, "an_ChangeSplineTypeNode", "Change Type")
        insertNode(layout, "an_ChangeSplineDirectionNode", "Change Direction")
        insertNode(layout, "an_ReplicateSplineNode", "Replicate")
        insertNode(layout, "an_OffsetSplineNode", "Offset Spline")
        layout.separator()
        insertNode(layout, "an_SplineInfoNode", "Info")
        insertNode(layout, "an_EvaluateSplineNode", "Evaluate")
        insertNode(layout, "an_ProjectOnSplineNode", "Project")
        insertNode(layout, "an_GetSplineLengthNode", "Get Length")
        layout.separator()
        insertNode(layout, "an_CurveObjectOutputNode", "Object Output")
        layout.separator()
        insertNode(layout, "an_LoftSplinesNode", "Loft")
        insertNode(layout, "an_RevolveSplineNode", "Revolve")

class GPencilMenu(bpy.types.Menu):
    bl_idname = "AN_MT_gpencil_menu"
    bl_label = "GPencil Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_GPObjectInputNode", "Object Input")
        insertNode(layout, "an_GPLayerInfoNode", "Layer Info")
        insertNode(layout, "an_GPFrameInfoNode", "Frame Info")
        insertNode(layout, "an_GPStrokeInfoNode", "Stroke Info")
        layout.separator()
        insertNode(layout, "an_SetGPLayerAttributesNode", "Set Layer Attributes")
        insertNode(layout, "an_ReplicateGPLayerNode", "Replicate Layer")
        insertNode(layout, "an_TransformGPLayerNode", "Transform Layer")
        insertNode(layout, "an_OffsetGPLayerFramesNode", "Offset Layer Frames")
        layout.separator()
        insertNode(layout, "an_SetGPStrokeAttributesNode", "Set Stroke Attributes")
        insertNode(layout, "an_ReplicateGPStrokeNode", "Replicate Stroke")
        insertNode(layout, "an_TransformGPStrokeNode", "Transform Stroke")
        insertNode(layout, "an_OffsetGPStrokeNode", "Offset Stroke")
        insertNode(layout, "an_ChangeGPStrokeDirectionNode", "Change Stroke Direction")
        layout.separator()
        insertNode(layout, "an_GPStrokeFromPointsNode", "Stroke From Points")
        insertNode(layout, "an_GPStrokeFromSplineNode", "Stroke From Spline")
        insertNode(layout, "an_GPFrameFromStrokesNode", "Frame From Strokes")
        insertNode(layout, "an_GPLayerFromFramesNode", "Layer From Frames")
        insertNode(layout, "an_GPObjectOutputNode", "Object Output")
        layout.separator()
        insertNode(layout, "an_GPMaterialOutputNode", "GP Material Output")
        insertNode(layout, "an_ObjectMaterialOutputNode", "Object Material Output")

class ActionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_action_menu"
    bl_label = "Action Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ActionFromObjectNode", "Action From Object")
        layout.separator()
        insertNode(layout, "an_ChainActionsNode", "Chain Actions")
        insertNode(layout, "an_DelayActionNode", "Delay Action")
        insertNode(layout, "an_OverlayActionNode", "Overlay Action")
        insertNode(layout, "an_WiggleActionNode", "Wiggle Action")
        insertNode(layout, "an_FollowSplineActionNode", "Follow Spline Action")
        layout.separator()
        insertNode(layout, "an_ObjectActionOutputNode", "Object Action Output")

class AnimationMenu(bpy.types.Menu):
    bl_idname = "AN_MT_animation_menu"
    bl_label = "Animation Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_TimeInfoNode", "Time Info")
        insertNode(layout, "an_DelayTimeNode", "Delay")
        insertNode(layout, "an_RepeatTimeNode", "Repeat")
        layout.separator()
        for dataType in numericalDataTypes:
            insertNode(layout, "an_AnimateDataNode", "Animate " + dataType, {"dataType" : repr(dataType)})
        layout.separator()
        for dataType in numericalDataTypes:
            insertNode(layout, "an_MixDataListNode", "Mix " + dataType + " List", {"dataType" : repr(dataType)})

class InterpolationMenu(bpy.types.Menu):
    bl_idname = "AN_MT_interpolation_menu"
    bl_label = "Interpolation Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ConstructInterpolationNode", "Construct")
        insertNode(layout, "an_InterpolationFromCurveNode", "From Curve")
        insertNode(layout, "an_InterpolationFromFCurveNode", "From FCurve")
        insertNode(layout, "an_MixInterpolationNode", "Mix")
        insertNode(layout, "an_MirrorInterpolationNode", "Mirror Interpolation")
        layout.separator()
        insertNode(layout, "an_EvaluateInterpolationNode", "Evaluate")
        insertNode(layout, "an_MapRangeNode", "Map Range", {"useInterpolation" : repr(True)})

class FalloffMenu(bpy.types.Menu):
    bl_idname = "AN_MT_falloff_menu"
    bl_label = "Falloff Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_FadeFalloffNode", "Fade")
        insertNode(layout, "an_DelayFalloffNode", "Delay")
        insertNode(layout, "an_WiggleFalloffNode", "Wiggle")
        insertNode(layout, "an_RandomFalloffNode", "Random")
        insertNode(layout, "an_NoiseFalloffNode", "Noise Falloff")
        insertNode(layout, "an_IndexMaskFalloffNode", "Index Mask")
        insertNode(layout, "an_ObjectControllerFalloffNode", "Object Controller")
        insertNode(layout, "an_SoundFalloffNode", "Sound")
        insertNode(layout, "an_SplineFalloffNode", "Spline")
        insertNode(layout, "an_MeshFalloffNode", "Mesh Falloff")
        layout.separator()
        insertNode(layout, "an_ConstantFalloffNode", "Constant")
        insertNode(layout, "an_CustomFalloffNode", "Custom")
        layout.separator()
        insertNode(layout, "an_DirectionalFalloffNode", "Directional")
        insertNode(layout, "an_PointDistanceFalloffNode", "Point Distance")
        insertNode(layout, "an_RadialFalloffNode", "Radial")
        layout.separator()
        insertNode(layout, "an_ClampFalloffNode", "Clamp")
        insertNode(layout, "an_InterpolateFalloffNode", "Interpolate")
        insertNode(layout, "an_RemapFalloffNode", "Remap")
        insertNode(layout, "an_InvertFalloffNode", "Invert")
        insertNode(layout, "an_MixFalloffsNode", "Mix")
        layout.separator()
        insertNode(layout, "an_EvaluateFalloffNode", "Evaluate")

class MaterialMenu(bpy.types.Menu):
    bl_idname = "AN_MT_material_menu"
    bl_label = "Material Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Material Input", {"assignedType" : repr("Material")})
        insertNode(layout, "an_ObjectMaterialInputNode", "Object Material Input")
        insertNode(layout, "an_BlendDataByNameNode", "Material By Name", {"dataType" : repr("Material")})
        insertNode(layout, "an_ObjectMaterialOutputNode", "Object Material Output")
        insertNode(layout, "an_MaterialOutputNode", "Material Output")
        insertNode(layout, "an_CyclesMaterialOutputNode", "Cycles Material Output")
        insertNode(layout, "an_GPMaterialOutputNode", "GP Material Output")
        insertNode(layout, "an_SetPolygonMaterialIndexNode", "Set Polygon Material Index")

class ParticleSystemMenu(bpy.types.Menu):
    bl_idname = "AN_MT_particle_system_menu"
    bl_label = "Particle System Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ParticleSystemsFromObjectNode", "From Object")
        insertNode(layout, "an_ParticleSystemParticlesDataNode", "Particles Data")
        insertNode(layout, "an_ParticleSystemHairDataNode", "Hair Data")

class FCurveMenu(bpy.types.Menu):
    bl_idname = "AN_MT_fcurve_menu"
    bl_label = "FCurve Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_FCurvesFromObjectNode", "From Object")
        insertNode(layout, "an_EvaluateFCurveNode", "Evaluate")
        insertNode(layout, "an_EvaluateFCurvesTransformsNode", "Evaluate Transforms")
        insertNode(layout, "an_FCurveInfoNode", "Info")
        insertNode(layout, "an_FCurveKeyframesNode", "Keyframes")

class SoundMenu(bpy.types.Menu):
    bl_idname = "AN_MT_sound_menu"
    bl_label = "Sound Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SoundFromSequenceNode", "Sound From Sequence")
        insertNode(layout, "an_SoundSpectrumNode", "Sound Spectrum")
        layout.separator()
        insertNode(layout, "an_ReadMIDIFileNode", "Read MIDI File")
        insertNode(layout, "an_MIDITrackInfoNode", "MIDI Track Info")
        insertNode(layout, "an_MIDINoteInfoNode", "MIDI Note Info")
        insertNode(layout, "an_MIDITempoEventInfoNode", "MIDI Tempo Event Info")
        insertNode(layout, "an_MIDITimeSignatureInfoNode", "MIDI Time Signature Event Info")
        insertNode(layout, "an_EvaluateMIDITrackNode", "Evaluate MIDI Track")

class SequenceMenu(bpy.types.Menu):
    bl_idname = "AN_MT_sequence_menu"
    bl_label = "Sequence Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SequencesFromChannelNode", "Sequences from Channel")
        insertNode(layout, "an_GetAllSequencesNode", "Get All Sequences")
        insertNode(layout, "an_TextSequenceOutputNode", "Text Sequence Output")
        insertNode(layout, "an_SequenceInfoNode", "Sequence Info")

class GeometryMenu(bpy.types.Menu):
    bl_idname = "AN_MT_geometry_menu"
    bl_label = "Geometry Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ConvertPlaneTypeNode", "Convert Plane Type")
        insertNode(layout, "an_PointListNormalNode", "Point List Normal")
        layout.separator()
        insertNode(layout, "an_ProjectPointOnLineNode", "Project Point on Line")
        insertNode(layout, "an_ProjectPointOnPlaneNode", "Project Point on Plane")
        insertNode(layout, "an_PointInCameraFrustrumNode", "Point in Camera Frustrum")
        layout.separator()
        insertNode(layout, "an_IntersectLineLineNode", "Intersect Line Line")
        insertNode(layout, "an_IntersectLinePlaneNode", "Intersect Line Plane")
        insertNode(layout, "an_IntersectLineSphereNode", "Intersect Line Sphere")
        insertNode(layout, "an_IntersectPlanePlaneNode", "Intersect Plane Plane")
        insertNode(layout, "an_IntersectSpherePlaneNode", "Intersect Sphere Plane")
        insertNode(layout, "an_IntersectSphereSphereNode", "Intersect Sphere Sphere")
        layout.separator()
        insertNode(layout, "an_BMeshTriangulateNode", "Triangulate BMesh")

class KDTreeAndBVHTreeMenu(bpy.types.Menu):
    bl_idname = "AN_MT_kdtree_bvhtree_menu"
    bl_label = "KDTree and BVHTree Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ConstructKDTreeNode", "Construct KDTree")
        insertNode(layout, "an_FindNearestPointInKDTreeNode", "Find Nearest")
        insertNode(layout, "an_FindNearestNPointsInKDTreeNode", "Find Amount")
        insertNode(layout, "an_FindPointsInRadiusInKDTreeNode", "Find in Radius")
        layout.separator()
        insertNode(layout, "an_ConstructBVHTreeNode", "Construct BVHTree")
        insertNode(layout, "an_RayCastBVHTreeNode", "Ray Cast")
        insertNode(layout, "an_FindNearestSurfacePointNode", "Find Nearest")
        insertNode(layout, "an_IsInsideVolumeBVHTreeNode", "Is Inside Volume")

class ViewerMenu(bpy.types.Menu):
    bl_idname = "AN_MT_viewer_menu"
    bl_label = "Viewer Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ViewerNode", "Viewer")
        insertNode(layout, "an_Viewer3DNode", "3D Viewer")
        insertNode(layout, "an_LoopViewerNode", "Loop Viewer")
        insertNode(layout, "an_InterpolationViewerNode", "Interpolation Viewer")
        insertNode(layout, "an_ActionViewerNode", "Action Viewer")

class SubprogramsMenu(bpy.types.Menu):
    bl_idname = "AN_MT_subprograms_menu"
    bl_label = "Subprograms Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_InvokeSubprogramNode", "Invoke Subprogram")
        subprograms = getSubprogramNetworks()
        if len(subprograms) == 0:
            layout.label(text = "   There are no subprograms yet")
        else:
            for network in sorted(subprograms, key = lambda x: x.name.lower()):
                insertNode(layout, "an_InvokeSubprogramNode", "-  " + network.name, {"subprogramIdentifier" : repr(network.identifier)})
        layout.separator()
        insertNode(layout, "an_GroupInputNode", "Group")
        insertNode(layout, "an_LoopInputNode", "Loop")
        insertNode(layout, "an_ScriptNode", "Script")
        layout.separator()
        insertNode(layout, "an_ExpressionNode", "Expression")
        layout.separator()
        insertNode(layout, "an_ViewportInputNode", "Viewport Input")
        insertNode(layout, "an_DataInterfaceNode", "Data Interface")

class LayoutMenu(bpy.types.Menu):
    bl_idname = "AN_MT_layout_menu"
    bl_label = "Layout Menu"

    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text = "Frame")
        props.use_transform = True
        props.type = "NodeFrame"
        props = layout.operator("node.add_node", text = "Reroute")
        props.use_transform = True
        props.type = "NodeReroute"


def insertNode(layout, type, text, settings = {}, icon = "NONE"):
    operator = layout.operator("node.add_node", text = text, icon = icon)
    operator.type = type
    operator.use_transform = True
    for name, value in settings.items():
        item = operator.settings.add()
        item.name = name
        item.value = value
    return operator

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)

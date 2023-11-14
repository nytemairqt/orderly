#--------------------------------------------------------------
# Meta Dictionary
#--------------------------------------------------------------

bl_info = {
	'name' : 'Orderly',
	'author' : 'SceneFiller',
	'version' : (1, 0, 0),
	'blender' : (3, 3, 0),
	'location' : 'View3d > Tool',
	'warning' : '',
	'wiki_url' : '',
	'category' : '3D View',
}

#--------------------------------------------------------------
# Import
#--------------------------------------------------------------

import os
import bpy

import bpy_extras
import math 
import importlib 

from mathutils import Vector
from bpy_extras import view3d_utils
from bpy_extras.io_utils import ImportHelper
from bpy_extras.image_utils import load_image

# Functions ---------------------- 

def ORDERLY_FN_analyzeObjects():
	return

def ORDERLY_FN_analyzeImages():
	# for image in scene.images 
	# add ram usage to list, keep index
	# filter list by largest ram value
	# return list
	return 

def ORDERLY_FN_optimizeObject():
	return

def ORDERLY_FN_optimizeImage():
	return 

# Classes ---------------------- 

class ORDERLY_OT_analyzeObjects(bpy.types.Operator):
	# Analyzes Mesh Objects and returns a list of High RAM Offenders
	bl_idname = 'orderly.analyze_objects'
	bl_label = ''
	bl_options = {'REGISTER', 'UNDO'}
	bl_description = 'Analyzes Mesh Objects and returns a list of High RAM Offenders'

	def execute(self, context):
		ORDERLY_FN_analyzeObjects()
		return{'FINISHED'}

class ORDERLY_OT_analyzeImages(bpy.types.Operator):
	# Analyzes Images and returns a list of High RAM Offenders
	bl_idname = 'orderly.analyze_images'
	bl_label = ''
	bl_options = {'REGISTER', 'UNDO'}
	bl_description = 'Analyzes Images and returns a list of High RAM Offenders'

	def execute(self, context):
		ORDERLY_FN_analyzeImages()
		return{'FINISHED'}

class ORDERLY_OT_optimizeObject(bpy.types.Operator):
	# Optimizes selected Mesh Object
	bl_idname = 'orderly.optimize_object'
	bl_label = ''
	bl_options = {'REGISTER', 'UNDO'}
	bl_description = 'Optimizes selected Mesh Object'

	def execute(self, context):
		ORDERLY_FN_optimizeObject()
		return{'FINISHED'}

class ORDERLY_OT_optimizeImage(bpy.types.Operator):
	# Optimizes selected Image
	bl_idname = 'orderly.optimize_image'
	bl_label = ''
	bl_options = {'REGISTER', 'UNDO'}
	bl_description = 'Optimizes selected Image'

	def execute(self, context):
		ORDERLY_FN_optimizeImage()
		return{'FINISHED'}
	

#--------------------------------------------------------------
# Interface
#--------------------------------------------------------------

class ORDERLY_PT_panelMain(bpy.types.Panel):
	bl_label = 'Orderly'
	bl_idname = 'ORDERLY_PT_panelMain'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Orderly'

	def draw(self, context):
		layout = self.layout	

class ORDERLY_PT_analyzeScene(bpy.types.Panel):
	bl_label = 'Analyze'
	bl_idname = 'ORDERLY_PT_analyzeScene'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Orderly'
	bl_parent_id = 'ORDERLY_PT_panelMain'

	def draw(self, context):
		layout = self.layout

		row = layout.row()
		row.label(text='Analyze')
		row.operator(ORDERLY_OT_analyzeObjects.bl_idname, text='Analyze Objects', icon='QUESTION')
		

#--------------------------------------------------------------
# Register 
#--------------------------------------------------------------

classes_interface = (ORDERLY_PT_panelMain, ORDERLY_PT_analyzeScene)
classes_functionality = (ORDERLY_OT_analyzeObjects, ORDERLY_OT_analyzeImages, ORDERLY_OT_optimizeObject, ORDERLY_OT_optimizeImage)

def register():

	# Register Classes
	for c in classes_interface:
		bpy.utils.register_class(c)
	for c in classes_functionality:
		bpy.utils.register_class(c)

def unregister():

	# Unregister
	for c in reversed(classes_interface):
		bpy.utils.unregister_class(c)
	for c in reversed(classes_functionality):
		bpy.utils.unregister_class(c)

if __name__ == '__main__':
	register()
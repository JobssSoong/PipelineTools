import os

# Substance Painter modules
import substance_painter as sp

# PySide module to build custom UI
from PySide2 import QtWidgets


plugin_widgets = []


def export_textures() :
	# Verify if a project is open before trying to export something
	if not sp.project.is_open() :
		return

	# Get the currently active layer stack (paintable)
	stack = sp.textureset.get_active_stack()

	# Get the parent Texture Set of this layer stack
	material = stack.material()

	# Build Export Preset resource URL
	export_preset = sp.resource.ResourceID.from_url('resource://shelf/Arnold_Pipeline')

	print( "Preset:" )
	print( export_preset.url() )

	# Setup the export settings
	resolution = material.get_resolution()
	
	# Setup the export path, in this case the textures
	# will be put next to the spp project file on the disk
	Path = sp.project.file_path()
	Path = os.path.dirname(Path) + "/image"
	if not os.path.exists(Path):
		os.makedirs(Path)

	# Build the configuration
	config = {
		"exportShaderParams" 	: False,
		"exportPath" 			: Path,
		"exportList"			: [ { "rootPath" : str(stack) } ],
		"exportPresets" 		: [ { "name" : "default", "maps" : [] } ],
		"defaultExportPreset" 	: export_preset.url(),
		"exportParameters" 		: [
			{
				"parameters"	: {
					"fileFormat" : "png",
					"bitDepth" : "8",
					"dithering": True,
					"paddingAlgorithm": "infinite" 
					}
			}
		]
	}

	sp.export.export_project_textures( config )

	for i in os.listdir(Path):
		if '_totex_' in i:
			src = Path+'/'+i
			dst = Path+'/'+i.replace('_totex_','_')
			try:
				os.rename(src,dst)
			except:
				pass


def start_plugin():
	# Create a text widget for a menu
	Action = QtWidgets.QAction("Custom Python Export", 
								triggered=export_textures)

	# Add this widget to the existing File menu of the application
	sp.ui.add_action(
		sp.ui.ApplicationMenu.File,
		Action )

	# Store the widget for proper cleanup later when stopping the plugin
	plugin_widgets.append(Action)


def close_plugin():
	# Remove all widgets that have been added from the UI
	for widget in plugin_widgets:
		sp.ui.delete_ui_element(widget)

	plugin_widgets.clear()


if __name__ == "__main__":
	start_plugin()

import loader_utils,loader_env

seg = ['ENV','PROP']
ver = ['layout_model','correct_model','high_model','tex']

for s in seg:
    for v in ver:
        assets_info = loader_utils.get_assets_info(s, v)
        for name in assets_info:
            #- Try Translate Preview into Specipied Size
            loader_utils.generate_specipied_preview(assets_info[name][1], loader_env.PREVIEW_SIZE)
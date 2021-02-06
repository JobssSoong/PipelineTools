def create_crypto_group():
    import cryptomatte_utilities as cu;
    import nuke
    s = nuke.selectedNode()
    s_x = s['xpos'].getValue()
    s_y = s['ypos'].getValue()
    c = cu.cryptomatte_create_gizmo();

    dot1 = nuke.nodes.Dot()
    dot1['xpos'].setValue(s_x + 34)
    dot1['ypos'].setValue(s_y + 30)
    dot1.setInput(0, s)

    dot2 = nuke.nodes.Dot()
    dot2['xpos'].setValue(s_x + 150 + 34)
    dot2['ypos'].setValue(s_y + 30)
    dot2.setInput(0, dot1)

    c['xpos'].setValue(s_x + 150)
    c['ypos'].setValue(s_y + 60)
    c.setInput(0, dot2)

    grade = nuke.nodes.Grade()
    grade['xpos'].setValue(s_x)
    grade['ypos'].setValue(s_y + 60)
    grade.setInput(0, dot1)
    grade.setInput(1, c)


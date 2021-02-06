
import nuke

toolbar = nuke.menu("Nodes")
menu = toolbar.addMenu("ACC", "ACC.png", index=-1)
menu.addCommand("AutoCom", "import AutoComp as ACC; ACC.AutoCreateCom();","F8")
menu.addCommand("Cryptomatte Group", "import CryptoGroup as cu; cu.create_crypto_group();","F7")

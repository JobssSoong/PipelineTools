# -*- coding: utf-8 -*-
import nuke
import nukescripts
import os

# Single Lighting Group
class LightingGroup(object):


    def __init__(self, lg_name, map_t,node_name_t,link_lst, x_ori=0, y_ori=0, x_space=150, y_space=120, output_is_dot=False, image_name = ""):
        self.lg_name = lg_name
        self.map_mat = map_t
        self.coord = [x_ori, y_ori]
        self.space = [x_space, y_space]
        self.lst = [[nuke.nodes.Dot()] * len(map[0]) for i in range(len(map))]
        self.NodesCreate(lg_name, map_t, node_name_t,x_ori, y_ori, x_space, y_space,output_is_dot=output_is_dot,image_name = image_name)
        self.LinkCreate(link_lst)
        self.__CleanUp()

    # Preset LG
    def __init__(self, lg_name, x_ori=0, y_ori=0, x_space=150, y_space=120, output_is_dot=False, image_name = ""):
        self.PresetDataInit(output_is_dot)
        self.coord = [x_ori, y_ori]
        self.space = [x_space, y_space]
        self.lst = [[nuke.nodes.Dot()] * len(self.map_mat[0]) for i in range(len(self.map_mat))]
        self.NodesCreate(lg_name, self.map_mat,self.node_name_mat, x_ori, y_ori, x_space, y_space,output_is_dot=output_is_dot,image_name = image_name)
        self.LinkCreate(self.link_lst)
        self.__CleanUp()

    # On Creation
    def NodesCreate(self, lg_name, map, node_names, x_ori, y_ori, x_space, y_space,output_is_dot,image_name):
        # Create node map
        for i in range(0, len(map)):
            for j in range(0, len(map[0])):
                if map[i][j] == "None":
                    continue
                try:
                    nuke.delete(self.lst[i][j])
                except:
                    pass
                self.lst[i][j] = eval("nuke.nodes." + map[i][j] + "()")
                if len(node_names[i][j]) == 3:
                    self.lst[i][j].knob('operation').setValue(node_names[i][j][0])
                    self.lst[i][j].knob('Achannels').setValue(node_names[i][j][1] + '_' + lg_name)
                    self.lst[i][j].knob('Bchannels').setValue(node_names[i][j][2])
                    self.lst[i][j].knob('label').setValue(node_names[i][j][1] + '_' + lg_name)
                    self.lst[i][j].knob('output').setValue("rgb")
                if len(node_names[i][j]) == 1:
                    if node_names[i][j][0].endswith('albedo'):
                        self.lst[i][j].knob('in').setValue(node_names[i][j][0])
                        self.lst[i][j].knob('label').setValue(node_names[i][j][0])
                    else:
                        self.lst[i][j].knob('in').setValue(node_names[i][j][0] + '_' + lg_name)
                        self.lst[i][j].knob('label').setValue(node_names[i][j][0] + '_' + lg_name)
                if len(node_names[i][j]) == 2:
                    self.lst[i][j].knob('operation').setValue(node_names[i][j][0])
                    self.lst[i][j].knob('output').setValue("rgb")
                w = self.lst[i][j].screenWidth()
                h = self.lst[i][j].screenHeight()
                self.lst[i][j].setXYpos(x_ori + x_space * j - w / 2, y_ori + y_space * i - h / 2)

        # Create input node
        #self.unpremult_node = nuke.nodes.Unpremult()
        #u_w = self.unpremult_node.screenWidth()
        #u_h = self.unpremult_node.screenHeight()
        #self.unpremult_node["channels"].setValue("all")
        #self.unpremult_node.setXYpos(x_ori - u_w / 2, y_ori - y_space - u_h / 2)
        self.input_node = nuke.nodes.Dot()
        self.input_node["label"].setValue(lg_name.upper() + '_input')
        self.input_node["note_font_size"].setValue(60)
        self.input_node.setXYpos(x_ori - x_space - 50, y_ori-5)

        #self.unpremult_node = nuke.nodes.Unpremult()
        #u_h = self.unpremult_node.screenHeight()
        #self.unpremult_node["channels"].setValue("all")
        #self.unpremult_node.setXYpos(int(x_ori - x_space), int(y_ori-5-u_h/2))
        #self.unpremult_node.setInput(0,self.input_node)
        self.lst[0][0].setInput(0, self.input_node)
        # Create output node
        self.lst[5][10].setXYpos(int(self.lst[5][10]['xpos'].getValue())+250, int(self.lst[4][10]['ypos'].getValue()))

        # Create back drop
        #self.back_drop = nuke.nodes.BackdropNode()
        #self.back_drop["bdwidth"].setValue(x_space * len(map[0]) + 100)
        #self.back_drop["bdheight"].setValue(y_space * len(map) + 500)
        #self.back_drop["tile_color"].setValue(893141759)
        #self.back_drop["label"].setValue(lg_name.upper())
        #self.back_drop["note_font"].setValue("Verdana Bold")
        #self.back_drop["note_font_size"].setValue(60)
        #self.back_drop.setXYpos(x_ori - 100, y_ori - 300)

        # for i in range(0,len(map)):
        #    for j in range(0,len(map[0])):
        #        if map[i][j] == "None":
        #            nuke.delete(self.lst[j][i])

        return self.lst

    def GetSpace(self):
        return [self.space[0]*len(self.map_mat[0]),self.space[1]*len(self.map_mat)]

    def GetInputNode(self):
        return self.input_node

    def GetOutputNode(self):
        return self.lst[5][10]

    def SetBDColor(self,cl):
        self.back_drop["tile_color"].setValue(cl)
        return

    def LinkCreate(self, link_lst):
        if self.lst is None:
            return
        for link in link_lst:
            self.lst[link[0][1]][link[0][0]].setInput(self.lst[link[0][1]][link[0][0]].inputs(),
                                                      self.lst[link[1][1]][link[1][0]])

    def Transform(self, x, y):
        for rol in self.lst:
            for i in rol:
                try:
                    i.setXYpos(int(i["xpos"].getValue() + x), int(i["ypos"].getValue() + y))
                except:
                    pass
        #self.back_drop.setXYpos(int(self.back_drop["xpos"].getValue() + x), int(self.back_drop["ypos"].getValue() + y))
        self.input_node.setXYpos(int(self.input_node["xpos"].getValue() + x), int(self.input_node["ypos"].getValue() + y))
        #self.unpremult_node.setXYpos(int(self.unpremult_node["xpos"].getValue() + x), int(self.unpremult_node["ypos"].getValue() + y))

    def PresetDataInit(self,output_is_dot):
        # Node array
        self.map_mat = [["Dot", "Dot", "Dot", "Dot", "Dot", "Dot", "Dot", "Dot", "Dot", "Dot", "Dot", "Dot"],
                        ["Merge2", "Merge2", "Shuffle", "Merge2", "Merge2", "Shuffle", "Shuffle", "Shuffle", "Shuffle",
                         "Shuffle",
                         "Shuffle", "Shuffle"],
                        ["Dot", "Merge2", "None", "Dot", "Merge2", "None", "None", "None", "None", "None", "None",
                         "None"],
                        ["None", "Merge2", "Dot", "None", "Merge2", "Dot", "Merge2", "Dot", "Merge2", "Dot", "Merge2",
                         "Dot"],
                        ["None", "Dot", "None", "None", "Merge2", "None", "Merge2", "None", "Merge2", "None", "Merge2",
                         "None"],
                        ["None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "Merge2",
                         "None"], ]

        # channels and names array
        self.node_name_mat = [[[], [], [], [], [], [], [], [], [], [], [], []],

                              [["divide", "diffuse_direct", "diffuse_albedo"],
                               ["divide", "diffuse_indirect", "diffuse_albedo"],
                               ["diffuse_albedo"], ["divide", "sss_direct", "sss_albedo"],
                               ["divide", "sss_indirect", "sss_albedo"],
                               ["sss_albedo"], ["specular_direct"], ["specular_indirect"], ["coat_direct"],
                               ["coat_indirect"],
                               ["transmission_direct"], ["transmission_indirect"]],

                              [[], ["plus", "diffuse_lgt"], [], [], ["plus", "sss_lgt"], [], [], [], [], [], [], []],

                              [[], ["multiply", "diffuse"], [], [], ["multiply", "sss"], [], ["plus", "specular"], [],
                               ["plus", "coat"],
                               [], ["plus", "transmission"], []],

                              [[], [], [], [], ["plus", "none"], [], ["plus", "none"], [], ["plus", "none"], [],
                               ["plus", "none"], []],

                              [[], [], [], [], [], [], [], [], [], [], ["plus","Merge2"], []], ]

        # link / relation array
        self.link_lst = [[(1, 4), (1, 3)], [(1, 0), (0, 0)], [(2, 0), (1, 0)], [(1, 3), (1, 2)], [(1, 3), (2, 3)],
                         [(1, 2), (1, 1)],
                         [(1, 2), (0, 2)], [(0, 2), (0, 1)], [(0, 1), (0, 0)], [(1, 1), (1, 0)], [(2, 3), (2, 1)],
                         [(2, 1), (2, 0)],
                         [(3, 2), (3, 1)], [(3, 1), (3, 0)], [(3, 0), (2, 0)], [(4, 4), (1, 4)], [(4, 4), (4, 3)],
                         [(4, 3), (4, 2)],
                         [(4, 3), (5, 3)], [(4, 2), (4, 1)], [(4, 2), (3, 2)], [(4, 1), (4, 0)], [(4, 0), (3, 0)],
                         [(5, 3), (5, 1)],
                         [(5, 1), (5, 0)], [(5, 0), (4, 0)], [(6, 3), (6, 1)], [(6, 3), (7, 3)],
                         [(6, 1), (6, 0)],
                         [(6, 0), (5, 0)], [(7, 3), (7, 1)], [(7, 1), (7, 0)], [(7, 0), (6, 0)],
                         [(8, 4), (6, 4)],
                         [(8, 3), (8, 1)], [(8, 3), (9, 3)], [(8, 1), (8, 0)], [(8, 0), (7, 0)], [(9, 3), (9, 1)],
                         [(9, 1), (9, 0)],
                         [(9, 0), (8, 0)], [(10, 4), (8, 4)], [(10, 4), (10, 3)], [(8, 4), (8, 3)], [(10, 3), (10, 1)],
                         [(10, 3), (11, 3)],
                         [(10, 1), (10, 0)], [(10, 0), (9, 0)], [(11, 3), (11, 1)], [(11, 1), (11, 0)],
                         [(11, 0), (10, 0)],
                         [(10, 5), (10, 4)], [(0, 1), (0, 0)], [(1, 1), (1, 0)], [(3, 1), (3, 0)], [(4, 1), (4, 0)],
                         [(6, 4), (4, 4)], [(6, 4), (6, 3)]]

        if output_is_dot is True:
            self.map_mat[5][10] = "Dot"
            self.node_name_mat[5][10] = []

    def Delete(self):
        for i in self.lst:
            for j in i:
                try:
                    nuke.delete(j)
                except:
                    pass
        try:
            nuke.delete(self.input_node)
        except:
            pass

    def __CleanUp(self):
        for i in range(0, len(self.map_mat)):
            for j in range(0, len(self.map_mat[0])):
                if self.map_mat[i][j] == "None":
                    try:
                        nuke.delete(self.lst[i][j])
                    except:
                        pass

# End Class

class StylizeModule(object):

    def __init__(self, startnode, name):
        module_path = os.path.dirname(os.path.realpath(__file__)) + '/stylizeModule.nk'
        nuke.scriptReadFile(module_path)
        self.startnode = startnode
        self.img_name = name
        self.__GetNewModule()
        self.__RenameModule()

        x_bias = startnode['xpos'].getValue()-self.node_lst[0]['xpos'].getValue()
        y_bias = startnode['ypos'].getValue() - self.node_lst[0]['ypos'].getValue()
        self.Transform(x_bias + 34, y_bias + 200)


    def __GetNewModule(self):

        nodes_name_lst = ['input','bd_big','bd_black_prev','bd_bloom','bd_style','bd_read_edge','read_edge','ep_RotoPaint','ep_Grade3','ep_Blur2','ep_d2',
                 'sm_d1','black_prev_d1','black_prev_d2','black_prev_shuffle','black_prev_main','black_prev_shadow','sm_d2','bloom_d1',
                 'bloom_d2','bloom_d3','bloom_Shuffle','bloom_d4','bloom_Glow1','bloom_Glow2','bloom_Convolve','sm_d3','sm_d4','sm_d5','ep_Grade1',
                 'ep_Dilate','ep_d1','ep_Blur1','ep_Grade2','ep_Merge','ep_Sharpen','output']
        self.node_lst = []
        for i in nodes_name_lst:
            self.node_lst.append(nuke.toNode(i))



    def __RenameModule(self):

        for i in self.node_lst:
            i['name'].setValue(i['name'].getValue()+'_'+self.img_name)



    def Transform(self, x, y):

        for i in self.node_lst:
            i['xpos'].setValue(i['xpos'].getValue()+x)
            i['ypos'].setValue(i['ypos'].getValue()+y)



    def GetInput(self):

        return self.node_lst[0]



    def GetOutput(self):

        return self.node_lst[-1]




# Entire com class
class CompFramework(object):

    def __init__(self,read_node):
        self.read_node = read_node

        self.black_level_node_path = os.path.dirname(os.path.realpath(__file__))+'\\blackLevelNode.nk'

        self.img_path = self.read_node["file"].getValue()
        self.img_name = self.img_path[self.img_path.rindex('/')+1:self.img_path.index('.',self.img_path.rindex('/'))]

        self.lighting_groups = [[],[],[],[],[]]
        self.unpremult_nodes = []
        self.dots = []
        self.aov_backdrops = []
        self.CreateFramework()
        self.__CreateOuterMerge()

    def CreateFramework(self):
        self.__GetProjectLayers()
        r_x = self.read_node["xpos"].getValue()
        r_y = self.read_node["ypos"].getValue()
        mid_x = r_x+self.read_node.screenWidth()/2

        # create reformat node
        self.reformat_node = nuke.nodes.Dot()
        self.reformat_node.setXYpos(int(r_x+34),int(r_y+200))
        self.reformat_node.setInput(0,self.read_node)
        self.read_backdrop_node = nuke.nodes.BackdropNode()
        self.read_backdrop_node["bdwidth"].setValue(800)
        self.read_backdrop_node["bdheight"].setValue(600)
        self.read_backdrop_node["tile_color"].setValue(0x32566eff)
        self.read_backdrop_node["label"].setValue("<font size=\"10\"><img src=\"Read.png\">\nRead\n")
        self.read_backdrop_node["note_font"].setValue("Verdana Bold")
        self.read_backdrop_node["border_width"].setValue(10)
        self.read_backdrop_node["note_font_size"].setValue(60)
        self.read_backdrop_node["name"].setValue(self.read_node['name'].getValue()+'_BD')
        self.read_backdrop_node.setXYpos(int(r_x - 400), int(r_y - 300))

        self.enter_AOV_node = nuke.nodes.Dot()


        # create lighting groups
        cur_lg_groups_num = 0
        self.aov_input_stack = []
        self.aov_output_stack = []
        for lg_index in range(0,len(self.lg_names)):

            if len(self.lg_names[lg_index])>0:

                x_pos = int(r_x - cur_lg_groups_num * 2300 - 2400)
                for i in range(0, len(self.lg_names[lg_index])):
                    if i == len(self.lg_names[lg_index]) - 1:
                        self.lighting_groups[lg_index].append(
                            LightingGroup(self.lg_names[lg_index][i], x_ori=x_pos, y_ori=int(r_y + 1200 - i * 900),
                                          output_is_dot=True, image_name=self.img_name))
                    else:
                        self.lighting_groups[lg_index].append(
                            LightingGroup(self.lg_names[lg_index][i], x_ori=x_pos, y_ori=int(r_y + 1200 - i * 900),
                                          output_is_dot=False, image_name=self.img_name))
                    self.lighting_groups[lg_index][i].Transform(0,(self.lg_max_num-1)*900)
                for i in range(1,len(self.lg_names[lg_index])):
                    self.lighting_groups[lg_index][i-1].GetInputNode().setInput(0,self.lighting_groups[lg_index][i].GetInputNode())
                    previous_out_node = self.lighting_groups[lg_index][i-1].GetOutputNode().input(0)
                    self.lighting_groups[lg_index][i - 1].GetOutputNode().setInput(1, previous_out_node)
                    self.lighting_groups[lg_index][i-1].GetOutputNode().setInput(0,self.lighting_groups[lg_index][i].GetOutputNode())


                # back drop
                back_drop = nuke.nodes.BackdropNode()
                self.aov_backdrops.append(back_drop)
                back_drop["bdwidth"].setValue(self.lighting_groups[lg_index][0].GetSpace()[0]+400)
                # note the width num
                self.child_lg_width = back_drop["bdwidth"].getValue()
                back_drop["bdheight"].setValue(900*self.lg_max_num+800)
                back_drop["tile_color"].setValue(741359359)
                if '_' in self.lg_names[lg_index][0]:
                    back_drop["label"].setValue(self.lg_names[lg_index][0][:self.lg_names[lg_index][0].rindex('_')].upper())
                else:
                    back_drop["label"].setValue(self.lg_names[lg_index][0].upper())
                back_drop["note_font"].setValue("Verdana Bold")
                back_drop["note_font_size"].setValue(100)
                back_drop.setXYpos(x_pos-300, int(r_y+600))


                self.aov_lg_input_node = nuke.nodes.Dot()
                self.aov_input_stack.append(self.aov_lg_input_node)
                if '_' in self.lg_names[lg_index][0]:
                    self.aov_lg_input_node["label"].setValue(self.lg_names[lg_index][0][:self.lg_names[lg_index][0].rindex('_')].upper()+"Input")
                else:
                    self.aov_lg_input_node["label"].setValue(self.lg_names[lg_index][0].upper() + "Input")
                self.aov_lg_input_node["note_font"].setValue("Verdana Bold")
                self.aov_lg_input_node["note_font_size"].setValue(80)
                self.aov_lg_input_node.setXYpos(int(self.lighting_groups[lg_index][0].GetInputNode()["xpos"].getValue()), int(r_y + 800 ))

                self.unpremult_nodes.append(nuke.nodes.Unpremult())
                self.unpremult_nodes[len(self.unpremult_nodes)-1]["channels"].setValue("all")
                self.unpremult_nodes[len(self.unpremult_nodes)-1].setXYpos(int(self.aov_lg_input_node["xpos"].getValue()-35), int(self.aov_lg_input_node["ypos"].getValue()+50))
                self.unpremult_nodes[len(self.unpremult_nodes)-1].setInput(0,self.aov_lg_input_node)

                self.lighting_groups[lg_index][len(self.lg_names[lg_index])-1].GetInputNode().setInput(0, self.unpremult_nodes[len(self.unpremult_nodes)-1])

                if lg_index != len(self.lg_names) - 1:  # judge if the node is a corner dot
                    self.aov_lg_output_node = nuke.nodes.Merge2()
                    self.aov_lg_output_node["operation"].setValue("plus")
                    self.aov_lg_output_node.setInput(1, self.lighting_groups[lg_index][0].GetOutputNode())
                    self.aov_lg_output_node.setXYpos(
                        int(self.lighting_groups[lg_index][0].GetOutputNode()["xpos"].getValue()+
                                self.lighting_groups[lg_index][0].GetOutputNode().screenWidth()/2-
                                self.aov_lg_output_node.screenWidth()/2),
                        int(r_y + 1000 + (self.lg_max_num) * 900))

                else:
                    self.aov_lg_output_node = nuke.nodes.Dot()
                    self.aov_lg_output_node.setInput(0, self.lighting_groups[lg_index][0].GetOutputNode())
                    self.aov_lg_output_node.setXYpos(
                        int(self.lighting_groups[lg_index][0].GetOutputNode()["xpos"].getValue()+36),
                        int(r_y + 1000 + (self.lg_max_num) * 900+40))

                self.aov_output_stack.append(self.aov_lg_output_node)

                if '_' in self.lg_names[lg_index][0]:
                    if nuke.toNode(self.img_name + '_' + self.lg_names[lg_index][0][:self.lg_names[lg_index][0].rindex('_')].upper()+"Output") == None:
                        self.aov_lg_output_node["name"].setValue(self.img_name + '_' + self.lg_names[lg_index][0][:self.lg_names[lg_index][0].rindex('_')].upper()+"Output")
                else:
                    if nuke.toNode(self.img_name + '_' + self.lg_names[lg_index][0].upper() + "Output") == None:
                        self.aov_lg_output_node["name"].setValue(self.img_name + '_' + self.lg_names[lg_index][0].upper() + "Output")
                self.aov_lg_output_node["note_font"].setValue("Verdana Bold")
                self.aov_lg_output_node["note_font_size"].setValue(80)

                cur_lg_groups_num += 1


        # lighting groups set links
        for i in range(1,len(self.aov_input_stack)):
            self.aov_output_stack[i-1].setInput(0,self.aov_output_stack[i])
            self.aov_input_stack[i].setInput(0, self.aov_input_stack[i-1])
        self.aov_input_stack[0].setInput(0,self.enter_AOV_node)

        # interval dot
        self.dots.append(nuke.nodes.Dot())
        self.dots[len(self.dots) - 1].setXYpos(int(mid_x-self.dots[len(self.dots) - 1].screenWidth()/2),int(r_y+800))
        self.dots[len(self.dots) - 1].setInput(0,self.reformat_node)

        self.enter_AOV_node.setXYpos(int(self.dots[len(self.dots) - 1]["xpos"].getValue()-300),int(self.dots[len(self.dots) - 1]["ypos"].getValue()))


        self.dots.append(nuke.nodes.Dot())
        self.dots[len(self.dots)-1].setXYpos(int(mid_x-self.dots[len(self.dots)-1].screenWidth()/2),int(self.enter_AOV_node["ypos"].getValue()))
        self.dots[len(self.dots)-1].setInput(0,self.dots[len(self.dots) - 2])
        self.enter_AOV_node.setInput(0,self.dots[len(self.dots)-1])

        self.dots.append(nuke.nodes.Dot())
        self.dots[len(self.dots) - 1].setXYpos(int(mid_x - self.dots[len(self.dots) - 1].screenWidth() / 2+400),
                                               int(self.enter_AOV_node["ypos"].getValue()))
        self.dots[len(self.dots) - 1].setInput(0, self.dots[len(self.dots) - 2])

        # create emission and alpha
        self.emission_unpremult_node = nuke.nodes.Unpremult()
        self.emission_unpremult_node["channels"].setValue("all")
        self.emission_unpremult_node.setXYpos(int(mid_x-self.emission_unpremult_node.screenWidth()/2),int(self.dots[1]["ypos"].getValue()+100))
        self.emission_unpremult_node.setInput(0,self.dots[1])

        self.emission_node = nuke.nodes.Shuffle()
        self.emission_node.knob('in').setValue("emission")
        self.emission_node.knob('label').setValue("emission")
        self.emission_node.setXYpos(int(mid_x - self.emission_node.screenWidth() / 2),
                                    int(self.dots[1]["ypos"].getValue() + 300))
        self.emission_node.setInput(0,self.emission_unpremult_node)

        self.emission_backdrop_node = nuke.nodes.BackdropNode()
        self.emission_backdrop_node["bdwidth"].setValue(500)
        self.emission_backdrop_node["bdheight"].setValue(900 * self.lg_max_num + 800)
        self.emission_backdrop_node["tile_color"].setValue(0x424242ff)
        self.emission_backdrop_node["label"].setValue("EMISSION")
        self.emission_backdrop_node["note_font"].setValue("Verdana Bold")
        self.emission_backdrop_node["note_font_size"].setValue(100)
        self.emission_backdrop_node.setXYpos(int(r_x - 200), int(r_y + 600))


        self.alpha_node = nuke.nodes.Shuffle()
        self.alpha_node.knob('in').setValue("alpha")
        self.alpha_node.knob('label').setValue("alpha")
        self.alpha_node.setXYpos(int(mid_x - self.emission_node.screenWidth() / 2+400),
                                               int(self.enter_AOV_node["ypos"].getValue()+300))
        self.alpha_node.setInput(0,self.dots[2])

        self.final_merge_node = nuke.nodes.Merge2()
        self.final_merge_node["operation"].setValue("plus")
        self.final_merge_node.setXYpos(int(mid_x - self.final_merge_node.screenWidth() / 2),
                                    int(self.aov_output_stack[0]["ypos"].getValue()+self.aov_output_stack[0].screenHeight()-50))
        self.final_merge_node.setInput(0, self.aov_output_stack[0])
        self.final_merge_node.setInput(1, self.emission_node)
        #self.final_merge_node

        # process alpha channel
        self.remove_node = nuke.nodes.Remove()
        self.remove_node.setXYpos(int(self.final_merge_node["xpos"].getValue()),int(self.final_merge_node["ypos"].getValue()+400))
        self.remove_node.setInput(0,self.final_merge_node)
        self.remove_node["operation"].setValue("keep")
        self.remove_node["channels"].setValue("rgb")

        self.copy_node = nuke.nodes.Copy()
        self.copy_node.setXYpos(int(self.remove_node["xpos"].getValue()),int(self.remove_node["ypos"].getValue()+100))
        self.copy_node.setInput(0,self.remove_node)

        self.dots.append(nuke.nodes.Dot())
        self.dots[len(self.dots) - 1].setXYpos(int(self.alpha_node["xpos"].getValue()+self.alpha_node.screenWidth()/2), int(self.copy_node["ypos"].getValue()+12))
        self.dots[len(self.dots) - 1].setInput(0, self.alpha_node)

        self.copy_node.setInput(1,self.dots[len(self.dots) - 1])
        self.copy_node["from0"].setValue("rgba.alpha")
        self.copy_node["to0"].setValue("rgba.alpha")
        self.copy_node["channels"].setValue("depth")

        # big back drop
        self.large_backdrop_node = nuke.nodes.BackdropNode()
        self.large_backdrop_node["bdwidth"].setValue((self.child_lg_width+100)*self.lighting_group_num+1500)
        self.large_backdrop_node["bdheight"].setValue(900 * self.lg_max_num + 1500)
        self.large_backdrop_node["tile_color"].setValue(893141759)
        self.large_backdrop_node["label"].setValue("Lighting Groups AOV")
        self.large_backdrop_node["note_font"].setValue("Verdana Bold")
        self.large_backdrop_node["note_font_size"].setValue(100)
        self.large_backdrop_node["z_order"].setValue(-2)
        self.large_backdrop_node.setXYpos(int(r_x - self.lighting_group_num * 2300 - 750), int(r_y + 400))

        # BlackLevels
        self.dots.append(nuke.nodes.Dot())
        self.dots[len(self.dots) - 1].setXYpos(int(self.copy_node["xpos"].getValue()+35),int(self.copy_node["ypos"].getValue()+300))
        self.dots[len(self.dots) - 1].setInput(0,self.copy_node)


        # final premultiply
        self.premult_node = nuke.nodes.Premult()
        self.premult_node.setXYpos(int(self.dots[len(self.dots) - 1]["xpos"].getValue())-35,int(self.dots[len(self.dots) - 1]["ypos"].getValue()+100))
        self.premult_node.setInput(0, self.dots[len(self.dots) - 1])

        # stylize module
        self.stylize_module = StylizeModule(self.premult_node, self.img_name)

    def GetName(self):
        return self.img_name

    def GetHeight(self):
        return 700 + 900 * self.lg_max_num + 1500 + 1100

    def __CreateOuterMerge(self):

        m = nuke.nodes.Merge2()
        m["note_font"].setValue("Verdana Bold")
        m["note_font_size"].setValue(60)
        m.setXYpos(int(self.stylize_module.GetOutput()["xpos"].getValue()+2000), int(self.stylize_module.GetOutput()["ypos"].getValue())-30)
        m.setInput(1, self.stylize_module.GetOutput())
        self.output_node = m

    def GetWidth(self):
        return 1

    def GetInputNode(self):
        return self.read_node

    def GetOutputNode(self):
        return self.output_node

    def Delete(self):
        for i in self.lighting_groups:
            for j in i:
                j.Delete()
        for i in self.dots:
            self.__DeleteNode(i)
        for i in self.aov_output_stack:
            self.__DeleteNode(i)
        for i in self.aov_input_stack:
            self.__DeleteNode(i)
        for i in self.aov_backdrops:
            self.__DeleteNode(i)
        for i in self.unpremult_nodes:
            self.__DeleteNode(i)

        self.__DeleteNode(self.reformat_node)
        self.__DeleteNode(self.read_backdrop_node)
        self.__DeleteNode(self.enter_AOV_node)
        self.__DeleteNode(self.emission_unpremult_node)
        self.__DeleteNode(self.emission_node)
        self.__DeleteNode(self.alpha_node)
        self.__DeleteNode(self.final_merge_node)
        self.__DeleteNode(self.remove_node)
        self.__DeleteNode(self.copy_node)
        self.__DeleteNode(self.large_backdrop_node)
        self.__DeleteNode(self.black_level_node)
        self.__DeleteNode(self.premult_node)
        self.__DeleteNode(self.black_level_backdrop_node)
        self.__DeleteNode(self.emission_backdrop_node)

    def IsEmpty(self):
        for i in self.lighting_groups:
            for j in i:
                if j != None:
                    return False
        return True

    def __DeleteNode(self,n):
        try:
            nuke.delete(n)
        except:
            pass


    def __GetProjectLayers(self):
        channel_lst = nuke.layers(self.read_node)
        #channel_lst = nuke.layers()
        self.lighting_group_num = 0
        #            key,fill,rim,env,fx
        self.preset_lg_names = ['rim','fill','env','key','fx']
        self.lg_names = [[],[],[],[],[]]
        self.lg_max_num = 0
        self.lg_nums = [0,0,0,0,0]
        for i in channel_lst:
            if i.startswith("diffuse_direct_") and i[15:] != "default":
                print i
                for j in range(0,len(self.preset_lg_names)):
                    if self.preset_lg_names[j] in i:
                        self.lg_names[j].append(i[15:])

        index = 0
        for i_lst in self.lg_names:

            self.lg_nums[index] = len(i_lst)
            index+=1

            if len(i_lst) != 0:
                self.lighting_group_num += 1

            if len(i_lst) > self.lg_max_num:
                self.lg_max_num = len(i_lst)

            i_lst.sort(reverse=True)
            print "LG recog: ",i_lst

        for i in range(0,5):
            try:
                self.lg_names.remove([])
            except:
                pass


# End Class


class ModalFramePanel( nukescripts.PythonPanel ):
    def __init__( self ):
        nukescripts.PythonPanel.__init__( self, "Warning" )

        self.kn = nuke.Tab_Knob("该图像已存在构建的面板！点击‘清理’清除已存在的面板")
        self.addKnob(self.kn)
        self.okButton = nuke.Script_Knob( "清理" )
        self.addKnob( self.okButton )
        self.okButton.setFlag( nuke.STARTLINE )
        self.cancelButton = nuke.Script_Knob( "取消" )
        self.addKnob( self.cancelButton )

    def knobChangedCallback(self, knob):
        self.knobChanged(knob)
        if knob == self.okButton:
            try:
                DeleteCom()
            except:
                pass
            self.finishModalDialog( True )
        elif knob == self.cancelButton:
            self.finishModalDialog( False)


    def accept(self):
        nuke.nodes.BackdropNode()

def DeleteTree(node):
    if node == None:
        return
    if node["name"].getValue()[:4] == "Read":
        return
    for i in range(0,node.inputs()):
        DeleteTree(node.input(i))
    try:
        nuke.delete(node)
    except:
        pass

def DeleteWholeTree():
    n = nuke.selectedNode()
    DeleteTree(n)

created_com_stack = []

def AutoCreateCom():
    global created_com_stack
    read = nuke.selectedNode()
    img_path = read["file"].getValue()
    img_name = img_path[img_path.rindex('/') + 1:img_path.index('.', img_path.rindex('/'))]
    for i in created_com_stack:
        print "%%%%%%%%%%%",i.GetName()
        if i.GetName() == img_name:
            print img_name
            ModalFramePanel().showModalDialog()
            return
    created_com_stack.append(CompFramework(read))

def DeleteCom():
    global created_com_stack
    read = nuke.selectedNode()
    img_path = read["file"].getValue()
    img_name = img_path[img_path.rindex('/') + 1:img_path.index('.', img_path.rindex('/'))]
    for i in created_com_stack:
        if i.GetName() == img_name:
            i.Delete()
            created_com_stack.remove(i)

def ComExists(read_node):
    return nuke.exists(read_node['name'].getValue + '_BG')





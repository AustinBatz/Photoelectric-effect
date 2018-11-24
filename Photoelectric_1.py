import ui
from scene import *
from datetime import datetime
from objc_util import UIApplication
import matplotlib.pyplot as plt
import photos
from numpy import pi

V_label = Texture('IMG_0004.PNG')

wait_time = 0
def _for(time, inclusive = True, reset = False):
	global wait_time
	
	if reset == True:
		wait_time = 0
		
	wait_time += time
	
	if not inclusive:
		return time
		
	return wait_time

class Scene_1(Scene):
	
	def setup(self):
		
		w = self.size.w # 1194
		h = self.size.h # 790
		
		self.background_color = 'black'
		self.all_nodes = Node()
		self.add_child(self.all_nodes)
		
		self.title = LabelNode('Photoelectric Effect',font=('<system>',100))
		self.add_child(self.title)
		self.title.anchor_point = (0.5,0.5)
		self.title.position = (w/2,3 * h/5)
		
		self.author = LabelNode('Austin Batz and Bennet Atwater',font=('<system>',50))
		self.title.add_child(self.author)
		self.author.anchor_point = (0.5,0.5)
		self.author.position = (0,-h/4)
		
		self.title.alpha = 0
		self.wait_1 = Action.wait(_for(1.5))
		self.fade_in_1 = Action.fade_to(1,_for(1))
		self.wait_2 = Action.wait(_for(3))
		self.fade_out_1 = Action.fade_to(0,_for(1))
		self.sequence_1 = Action.sequence(self.wait_1,self.fade_in_1,self.wait_2,self.fade_out_1)
		self.title.run_action(self.sequence_1)
		
class Scene_2(Scene):
	
	def setup(self):
		
		w = self.size.w # 1194
		h = self.size.h # 790
		
		self.background_color = 'black'
		self.all_nodes = Node()
		self.add_child(self.all_nodes)
		
		# Apparatus
		self.apparatus = Node()
		self.add_child(self.apparatus)
		# self.apparatus.z_position = 1
		
		# Vacuum tube
		self.tube = ShapeNode(ui.Path.oval(0,0,5 * w / 16,5 * h / 6))
		self.tube.anchor_point = (0.2,0.5)
		self.apparatus.position = (w/2,h/2)
		self.tube.fill_color = '#000000'
		self.tube.stroke_color = '#ffffff'
		self.tube.line_width = 6
		self.apparatus.add_child(self.tube)
		
		# Cathode
		self.cathode = ShapeNode(ui.Path.rect(0,0,150,10))
		self.cathode.anchor_point = (1,0.5)
		self.cathode.position = (5 * w / 32,1 * h / 6)
		self.apparatus.add_child(self.cathode)
		
		# Anode
		self.anode = ShapeNode(ui.Path.rect(0,0,150,10))
		self.anode.anchor_point = (1,0.5)
		self.anode.position = (5 * w / 32,-1 * h / 6)
		self.apparatus.add_child(self.anode)
		
		# Top wire
		self.top_wire_path = ui.Path.rect(0,0,5,225)
		self.top_wire_path.append_path(ui.Path.rect(-300,0,300,5))
		self.top_wire = ShapeNode(self.top_wire_path)
		self.top_wire.anchor_point = (1,0)
		self.top_wire.position = (self.cathode.position[0] - 150 / 2,self.cathode.position[1] + 4)
		self.apparatus.add_child(self.top_wire)
		
		# Bottom wire
		self.bottom_wire_path = ui.Path.rect(0,0,5,225)
		self.bottom_wire_path.append_path(ui.Path.rect(-300, 220 ,300,5))
		self.bottom_wire = ShapeNode(self.bottom_wire_path)
		self.bottom_wire.anchor_point = (1,1)
		self.bottom_wire.position = (self.anode.position[0] - 150 / 2,self.anode.position[1] - 4)
		self.apparatus.add_child(self.bottom_wire)
		
		# Battery
		self.battery = ShapeNode(ui.Path.oval(0,0,w/8,w/8))
		self.battery.position = (self.cathode.position[0] - 75 - 303,0)
		self.battery.fill_color = '#000000'
		self.battery.stroke_color = '#ffffff'
		self.battery.line_width = 6
		self.battery.anchor_point = (0.5,0.5)
		self.apparatus.add_child(self.battery)
		
		# Battery connector
		self.battery_connector_path = ui.Path.rect(0,w/16,5,285)
		self.battery_connector_path.append_path(ui.Path.rect(0,-w/16,5,-285))
		self.battery_connector = ShapeNode(self.battery_connector_path)
		self.battery_connector.position = (self.battery.position[0], 0)
		self.apparatus.add_child(self.battery_connector)
		
		# Voltage label
		self.V_label = SpriteNode(V_label)
		self.V_label.x_scale = 0.3
		self.V_label.y_scale = self.V_label.x_scale
		self.V_label.position = self.battery.position
		self.V_label_plus = LabelNode('+',font=('<system>',50))
		self.V_label_plus.position = (self.battery.position[0] - 40, self.battery.position[1] + 100)
		self.apparatus.add_child(self.V_label_plus)
		self.V_label_minus = LabelNode('-',font=('<system>',50))
		self.V_label_minus.position = (self.battery.position[0] - 40, self.battery.position[1] - 90)
		self.apparatus.add_child(self.V_label_minus)
		self.apparatus.add_child(self.V_label)
		
		# Cathode label
		self.node_labels = Node()
		self.cathode_label = LabelNode('Cathode',font=('<system>',50))
		self.cathode_label.anchor_point = (0,0)
		self.cathode_label.position = (280,230)
		self.cathode_line_path = ui.Path.oval(0,0,0,0)
		self.cathode_line_path.line_to(-130,100)
		self.cathode_line = ShapeNode(self.cathode_line_path)
		self.cathode_line.line_width = 4
		self.cathode_line.anchor_point = (1,1)
		self.cathode_line.position = (self.cathode_label.position[0] - 10, self.cathode_label.position[1] + 15)
		self.cathode_line.stroke_color = '#ffffff'
		self.node_labels.add_child(self.cathode_label)
		self.node_labels.add_child(self.cathode_line)
		self.apparatus.add_child(self.node_labels)
		
		# Anode label
		self.anode_label = LabelNode('Anode',font=('<system>',50))
		self.anode_label.anchor_point = (0,1)
		self.anode_label.position = (280,-230)
		self.anode_line_path = ui.Path.oval(0,0,0,0)
		self.anode_line_path.line_to(-130,-100)
		self.anode_line = ShapeNode(self.anode_line_path)
		self.anode_line.line_width = 4
		self.anode_line.anchor_point = (1,0)
		self.anode_line.position = (self.anode_label.position[0] - 10, self.anode_label.position[1] - 15)
		self.anode_line.stroke_color = '#ffffff'
		self.node_labels.add_child(self.anode_label)
		self.node_labels.add_child(self.anode_line)
		
		# Fade in apparatus
		self.apparatus.alpha = 0
		self.wait_1 = Action.wait(_for(1.5))
		self.fade_in_1 = Action.fade_to(1,_for(1,0))
		self.sequence_1 = Action.sequence(self.wait_1,self.fade_in_1)
		self.apparatus.run_action(self.sequence_1)
		
		# Cubic Bezier curve
		self.bezier_path = ui.Path.oval(0,0,0,0)
		for i in range(0,3):
			self.bezier_path.add_curve(200 + 200 * i,0,100 + 200 * i,200,100 + 200 * i,-200)
		self.bezier = ShapeNode(self.bezier_path)
		self.bezier.stroke_color = '#ffffff'
		self.bezier.fill_color = '#000000'
		self.bezier.position = (w/2,w/2)
		#self.add_child(self.bezier)
		
		self.bezier_2 = ShapeNode(self.sinusoid(400, 200, 10))
		self.bezier_2.stroke_color = '#ffffff'
		self.bezier_2.fill_color = '#000000'
		self.bezier_2.anchor_point = (0.5,1)
		self.bezier_2.position = (w/2,w/2)
		#self.add_child(self.bezier_2)
		
		# Classical description
		self.classical = Node()
		self.add_child(self.classical)
		
		# Classical label
		self.classical_label = LabelNode('Classical \nDescription', font=('<system>',70))
		self.classical_label.anchor_point = (0,1)
		self.classical_label.position = (20,h - 20)
		self.classical.add_child(self.classical_label)
		
		# Classical energy label
		self.classical_energy = LabelNode('KE \u221D Intesity', font=('<system>',65))
		self.classical_energy.anchor_point = (1,1)
		self.classical_energy.position = (w - 20,h - 20)
		self.classical.add_child(self.classical_energy)
		
		# Classical wave
		self.wave = ShapeNode(self.sinusoid(50,70,20))
		self.wave.position = (20,50)
		self.wave.anchor_point = (0,0.5)
		self.wave.fill_color = '#000000'
		self.wave.stroke_color = '#ffffff'
		self.wave.run_action(Action.rotate_by(-1 * pi / 4,0))
		self.wave.position = (self.cathode.position[0] + w/2 - 75 + w/2, self.cathode.position[1] + h/2 - w/2)
		self.classical.add_child(self.wave)
		
		# Classical electron
		self.classical_electron = ShapeNode(ui.Path.oval(0,0,10,10))
		self.classical_electron.position = (self.cathode.position[0] + w/2 - 80, self.cathode.position[1] + h/2)
		self.classical_electron.fill_color = '#ffffff'
		self.add_child(self.classical_electron)
		
		# Fade in classical description
		self.classical.alpha = 0
		self.wait_2 = Action.wait(_for(1))
		self.fade_in_2 = Action.fade_to(1,_for(1,0))
		self.sequence_2 = (self.wait_2, self.fade_in_2)
		self.classical.run_action(Action.sequence(self.sequence_2))
		self.wait_wave = Action.wait(_for(1))
		self.move_wave = Action.move_by(-w/2,w/2,_for(1,0),TIMING_SINODIAL)
		self.wave_sequence = (self.wait_wave, self.move_wave)
		self.wave.run_action(Action.sequence(self.wave_sequence))
		
		# Eject classical electron
		self.classical_electron.alpha = 0
		self.wait_3 = Action.wait(_for(0))
		self.fade_in_3 = Action.fade_to(1,_for(0,0))
		self.eject_classical = Action.move_to(self.classical_electron.position[0],self.classical_electron.position[1] - 2 *(self.classical_electron.position[1] - h/2),_for(1,0))
		self.sequence_3 = (self.wait_3,self.fade_in_3,self.eject_classical)
		self.classical_electron.run_action(Action.sequence(self.sequence_3))
		self.classical.add_child(self.classical_electron)
		
		# Fade out classical
		self.wait_4 = Action.wait(_for(1))
		self.classical_fade_out = Action.fade_to(0,_for(1,0))
		self.sequence_4 = (self.wait_4, self.classical_fade_out)
		self.classical.run_action(Action.sequence(self.sequence_4))
		
	def sinusoid(self,amplitude,period,cycles=1):
		
		path = ui.Path.oval(0,0,0,0)
		half_period = period / 2
		for i in range(0,cycles):
			path.add_curve(half_period * (1 + i), 0, half_period * (.5 + i), amplitude, half_period * (.5 + i), -1 * amplitude)
			
		return path
		
scene1 = Scene_1()
scene2 = Scene_2()

for My_Scene in [scene2]:#, scene2]:
	w, h = ui.get_screen_size()
	frame = (0,0,w,h)
	v = ui.View(frame=frame)
	scene_view = SceneView(frame=frame)
	scene_view.frame_interval=1
	scene_view.anti_alias=False
	scene_view.flex = 'WH'
	scene_view.scene = My_Scene#()
	v.add_subview(scene_view)
	v.present('fullscreen', hide_title_bar=True)
	UIApplication.sharedApplication().statusBar().hidden = True
	My_Scene.did_evaluate_actions()

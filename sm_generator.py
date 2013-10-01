from fluidity import StateMachine, state, transition

class SMGenerator():

	def __init__(self, data):
		self.data = data
		
	def __repr__(self):
		return "class Statemachine(StateMachine):"

	def get_states(self):
		list_states = []
		for layer in self.data.layers:
			for obj in layer.objects:
				if obj.type.name == "UML - State":
					print obj.properties["text"].value.text.strip()
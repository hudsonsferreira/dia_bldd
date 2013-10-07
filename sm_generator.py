class DataNotFoundException(Exception):
	pass

class SMGenerator():

	def __init__(self):
		self.header = "from fluidity import StateMachine, state, transition\nclass MyStateMachine(StateMachine):"
		self.data = None

	def load_data(self, data):
		self.data = data
	
	def _get_states(self):
		states = []
		for layer in self.data.layers:
			for obj in layer.objects:
				if obj.type.name == "UML - State":
					states.append(obj.properties["text"].value.text.strip())
		return states

	def _get_transitions(self):
		transitions = []
		for layer in self.data.layers:
			for obj in layer.objects:
				if obj.type.name == "UML - Transition":
					source = obj.handles[0].connected_to.object
					target = obj.handles[1].connected_to.object
					if source.type.name == "UML - State" and target.type.name == "UML - State":
						transitions.append({'from':source.properties["text"].value.text.strip(), 
										    'event':obj.properties["trigger"].value, 
										    'to':target.properties["text"].value.text.strip(), 
										    'guard':obj.properties["guard"].value})			
		return transitions				

	def _get_initial_state(self):
		for layer in self.data.layers:
			for obj in layer.objects:
				if obj.type.name == "UML - Transition":
					source = obj.handles[0].connected_to.object
					target = obj.handles[1].connected_to.object
					if source.type.name == "UML - State Term" and target.type.name == "UML - State":
						return target.properties["text"].value.text.strip()

	def generate(self):
		if self.data == None:
			raise DataNotFoundException("You should load some data!")
		content = self.header
		initial_state = self._get_initial_state()
		states = self._get_states()
		transitions = self._get_transitions()

		content += "\n\n\t\tinitial_state = '"+initial_state+"'\n"

		for state in states:
			content += "\n\t\tstate('"+state+"')"

		content += "\n"

		for transition in transitions:
			content += "\n\t\ttransition(from_='"+transition["from"]+"', event='"+transition["event"]+"', to='"+transition["to"]
			if transition["guard"] != "":
				content += "', guard='"+transition["guard"]
			content +="')"

		print content			
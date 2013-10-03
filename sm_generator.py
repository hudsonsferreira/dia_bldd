
class SMGenerator():

	def __init__(self, data):
		self.data = data
	
	def _get_states(self):
		print "\n"
		for layer in self.data.layers:
			for obj in layer.objects:
				if obj.type.name == "UML - State":
					print "\t\tstate('%s')" %(obj.properties["text"].value.text.strip())

	def _get_transitions(self):
		print "\n"
		for layer in self.data.layers:
			for obj in layer.objects:
				if obj.type.name == "UML - Transition":
					source = obj.handles[0].connected_to.object
					target = obj.handles[1].connected_to.object
					if source.type.name == "UML - State" and target.type.name == "UML - State":
						print "\t\ttransition(from='%s', event='%s', to='%s')" %(source.properties["text"].value.text.strip(), obj.properties["trigger"].value, target.properties["text"].value.text.strip())

	def generate(self):
		print "from fluidity import StateMachine, state, transition\nclass MyStateMachine(StateMachine):"
		self._get_states()
		self._get_transitions()
from statemachine_generator.sm_generator import SMGenerator

class SpecGenerator(SMGenerator):

	def __init__(self, data):
		self.data = data
		sm = SMGenerator()
		sm.load_data(data)
from dia_bldd_modules.statemachine_generator.sm_generator import SMGenerator

class SpecGenerator():

	def __init__(self, data):
		self.data = data
		self.sm = SMGenerator()
		self.sm.load_data(data)

	def create_initial_state_test(self):
		initial_state = self.sm._get_initial_state()
		phrase = 'initial_state |should_not| be_empty\n'+\
		         'initial_state |should| be(1)\n'+\
		         'initial_state |should| equal_to("%s")'%(initial_state)
		return phrase 